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
        return string[:-1]  # Remove trailing \n

    @property
    def won(self):
        # TODO - check for win state
        return False

    def changePlayer(self, num=1):
        self.player = ((self.player - 1 - num) % (len(self.players) - 1)) + 1

    def attemptMove(self, row, col):
        # Decrement numbers to conform to array indices
        row, col = row - 1, col - 1

        if self.board[row][col] == 0:
            self.board[row][col] = self.player
            return True
        return False

    def nextMove(self):
        print(f"\nPlayer {self.player}'s Turn:")
        print(f"\nWhere do you want to place an {self.players[self.player]}")
        print(self)

        validMove = None
        while not validMove:
            if validMove is not None:
                print("Invalid Move")
            rowNum = UI.getNum("Row Num", 1, self.boardSize)
            colNum = UI.getNum("Column Num", 1, self.boardSize)

            validMove = self.attemptMove(rowNum, colNum)

        self.changePlayer()

    def play(self):
        # Reset the board
        self.board = np.zeros((self.boardSize, self.boardSize), dtype=int)
        self.player = 1

        while not self.won:
            self.nextMove()

        # Undo moving to player after winning player
        self.changePlayer(num=-1)

        print(f"Player {self.player} won!!")


if __name__ == "__main__":
    currentBoard = Board()

    currentBoard.play()
