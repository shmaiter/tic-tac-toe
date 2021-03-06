import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()  # fill a list with 9 empty spaces
        self.current_winner = None

    @staticmethod
    def make_board():
        return [" " for _ in range(9)]

    def print_board(self):
        # Printing borders of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 which numbers correspond to their specific box or spot
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == " ":
        #         moves.append(i)
        # return moves
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        # check for winner in rows
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check for winner in columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check for winner in diagonals
        if square % 2 == 0:
            diagonal_TopL_BottomR = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal_TopL_BottomR]):
                return True
            diagonal_BottomL_TopR = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal_BottomL_TopR]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"  # startin letter

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        # gives a break between iteration for computer to respond. Like if it were thinking.
        time.sleep(1)

    if print_game:
        print("It\'s a tie")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = SmartComputerPlayer("O")

    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
