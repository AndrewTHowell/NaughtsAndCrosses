import numpy as np
import UI


class Board:

    def __init__(self, boardSize=3):
        self.boardSize = boardSize
        self.players = {
            0: " ",
            1: "O",
            2: "X"
        }

        self.board = np.zeros((self.boardSize, self.boardSize), dtype=int)
        self.player = 1

    def __str__(self):
        endCharacters = " |"
        string = ""
        for row in self.board:
            if string != "":
                string += ("-" * ((4 * self.boardSize) - 1)) + "\n"
            for cell in row:
                string += " " + self.players[cell] + endCharacters
            string = string[:-len(endCharacters)] + "\n"
        return string[:-2]  # Remove trailing \n

    @property
    def won(self):
        # TODO - check for win state
        return False

    def nextPlayer(self):
        self.player = (self.player % (len(self.players) - 1)) + 1

    def nextMove(self):
        print(f"\nPlayer {self.player}'s Turn:")
        print(f"\nWhere do you want to place an {self.players[self.player]}")
        print(self)
        rowNum = UI.getNum("Row Num", 1, self.boardSize)
        colNum = UI.getNum("Column Num", 1, self.boardSize)

        self.nextPlayer()

    def play(self):
        # Reset the board
        self.board = np.zeros((self.boardSize, self.boardSize), dtype=int)
        self.player = 1

        # while not self.won:
        for i in range(20):
            self.nextMove()


if __name__ == "__main__":
    currentBoard = Board()

    currentBoard.play()
