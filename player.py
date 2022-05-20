import math
import random


class Player:
    def __init__(self, letter):  # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")

        return val


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # randomly choose one
            square = random.choice(game.available_moves())
        else:
            # select the square based on the minimax algorithm
            square = self.minimax(game, self.letter)["position"]

        return square

    def minimax(self, game_state, player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X"

        # first chech if the previos move is a winner
        # this will be the base case
        if game_state.current_winner == other_player:
            return {"position": None,
                    "score": 1 * (game_state.num_empty_squares() + 1) if other_player == max_player else -1 * (game_state.num_empty_squares() + 1)
                    }
        elif not game_state.empty_squares():
            return {"position": None, "score": 0}

        if player == max_player:
            # each score should be maximize (be larger)
            best = {"position": None, "score": -math.inf}
        else:
            # each score shoul me minimize
            best = {"position": None, "score": math.inf}

        for possible_move in game_state.available_moves():
            # step 1: make a move try that spot
            game_state.make_move(possible_move, player)
            # step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(
                game_state, other_player)  # simulate the best

            # step 3: undo the move
            game_state.board[possible_move] = " "
            game_state.current_winner = None
            # this represents the move optimal next move
            sim_score["position"] = possible_move

#             # undo move
#             state.board[possible_move] = ' '
#             state.current_winner = None
#             # this represents the move optimal next move
#             sim_score['position'] = possible_move

            # step 4: update the dictionaries in the simulation encoutered a better score for movement
            if player == max_player:  # we need to maximize max player posibilities
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:  # but minimize the other player
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
