import numpy as np


class Board:

    def __init__(self, boardSize=3):

        self.boardSize = boardSize
        self.board = np.zeros((boardSize, boardSize), dtype=int)

        self.players = {
            0: " ",
            1: "O",
            2: "X"
        }

    def __str__(self):
        endCharacters = " |"
        string = ""
        for row in self.board:
            if string != "":
                string += ("-" * ((4 * self.boardSize) - 1)) + "\n"
            for cell in row:
                string += " " + self.players[cell] + endCharacters
            string = string[:-len(endCharacters)] + "\n"

        return string


if __name__ == "__main__":
    currentBoard = Board()
