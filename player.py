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

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        return self.minimax(game, self.letter)['position']

    def minimax(self, state, player):

        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        # base case:
        # the last move is made by the other player, we check that whether they have won
        if state.winner == other_player:
            score = 1*(state.get_num_empty_squares()+1) if other_player == max_player \
                    else -1*(state.get_num_empty_squares()+1)
            return {'position': None, 'score': score}
        elif not state.has_empty_squares():
            return {'position': None, 'score': 0}

        # initial value:
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        # recursive loop
        for next_move in state.get_available_moves():
            state.make_move(player, next_move)

            sim_game = self.minimax(state, other_player)
            # print(next_move)
            state.board[next_move] = ' '
            state.winner = None
            sim_game['position'] = next_move
            if player == max_player:
                if sim_game['score'] > best['score']:
                    best = sim_game
            else:
                if sim_game['score'] < best['score']:
                    best = sim_game
        return best

