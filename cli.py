import random
import numpy as np
class CliGame:
    def __init__(self):
        numbers = list(range(1, 19)) * 2
        random.shuffle(numbers)
        self.board = np.array(numbers).reshape(6, 6)
    def play(self):
        success = 0
        play_board = np.array([["HIDDEN"] * 6 for _ in range(6)])
        while success < 18:
            row1 = int(input("enter the row for the first guess: "))
            col1 = int(input("enter the col for the first guess: "))
            row2 = int(input("enter the row for the second guess: "))
            col2 = int(input("enter the col for the second guess: "))
            if row1 == row2 and col1 == col2:
                print("the two pairs have to be different, try again:")
                continue
            if self.board[row1][col1]==self.board[row2][col2]:
                play_board[row1][col1] = self.board[row1][col1]
                play_board[row2][col2] = self.board[row2][col2]
                success+=1
            print(play_board)

game = CliGame()
game.play()
print("you have finished the game.")