import numpy as np
import random
from abc import ABC, abstractmethod
class IinterfaceWithYourGame(ABC):
    @abstractmethod
    def insert_token(self,column=0,player=1):
        pass
    def get_win(self,player):
        pass

class Game(IinterfaceWithYourGame):
    def __init__(self):
        self._rows = 6
        self._columns = 7
        self._game_board = np.zeros((self._columns,self._rows))

    def insert_token(self,column=0,player=1):
        for i,index in enumerate(self._game_board):
            if column == i:
                vals = (index > 0).sum()
                if vals == self._rows:
                    print('No Space on this column')
                    self.print_board()
                    return False
                print(f'inserting in row: {i}')
                for j,sub_index in  reversed(list(enumerate(index))):
                    if index[j] == 0:
                        self._game_board[i][j] = player
                        self.print_board()
                        return True
       
    def print_board(self):
        temp_board = self._game_board
        print(np.transpose(temp_board))

    def get_win(self,player):
        for c in range(7):
            for r in range(3):
                if self._game_board[c][r] == player and self._game_board[c][r+1] == player and self._game_board[c][r+2] == player and self._game_board[c][r+3] == player:
                    return True
        for c in range(3):
            for r in range(6):
                if self._game_board[c][r] == player and self._game_board[c+1][r] == player and self._game_board[c+2][r] == player and self._game_board[c+3][r] == player:
                    return True

        for c in range(4):
            for r in range(3):
                if self._game_board[c][r] == player and self._game_board[c+1][r+1] == player and self._game_board[c+2][r+2] == player and self._game_board[c+3][r+3] == player:
                    return True
                
        for c in range(4):
            for r in range(3, 6):
                if self._game_board[c][r] == player and self._game_board[c+1][r-1] == player and self._game_board[c+2][r-2] == player and self._game_board[c+3][r-3] == player:
                    return True
# 
    
    def get_board(self):
        return self._game_board


class table:
    def __init__(self,Game):
        self._player_tracker = None
        self.who_goes_first()
        self._game = Game
    def who_goes_first(self):
        self._player_tracker = random.randint(1,2)
        print(f"Player: {self._player_tracker} goes first... Good luck")
    def get_turn(self):
        print(f"Player {self._player_tracker}'s turn")
        return self._player_tracker
    def get_input(self):
        print(f"Player {self._player_tracker} enter column: ")
        while True:
            try:
                num = int(input("Enter an integer 1-7: "))
            except ValueError:
                print("Please enter a valid integer 1-7")
                continue
            if num >= 1 and num <= 10:
                return num
            else:
                print('The integer must be in the range 1-10')

    def take_turn(self):
        column = self.get_input()
        while True:
            if self._game.insert_token(column,self._player_tracker):
                break
            else:
                column = self.get_input()
        if self._player_tracker == 1:
            self._player_tracker = 2
        else:
            self._player_tracker = 1



def main():
    connect_four = Game()
    mytable = table(connect_four)
    while True:
        mytable.take_turn()



if __name__=="__main__":
    main()