import math
import random

class Player:
    def __init__(self, letter):
        # X or O
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.get_available_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        
        valid_move = False
        while not valid_move:
            try:
                move = input("choose a number from 0-8: ")
                move = int(move)
                if move not in game.get_available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid square. Try again.")
        return move