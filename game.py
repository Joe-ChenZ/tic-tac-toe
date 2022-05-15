from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.winner = None

    def print_board(self):
        for i in range(3):
            print('| ' + ' | '.join(self.board[3*i: 3*i+3]) + ' |')
        print()

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def has_empty_squares(self):
        return ' ' in self.board

    def get_num_empty_squares(self):
        return len(self.get_available_moves())
    
    def make_move(self, letter, idx):
        if self.board[idx] == ' ':
            self.board[idx] = letter
            if (self.is_winner(idx, letter)):
                self.winner = letter
            return True
        return False
    def is_winner(self, idx, letter):
        # row
        row = idx // 3
        row_count = self.board[row*3: row*3+3]
        # print(row_count)
        if all([s == letter for s in row_count]):
            return True
        # col
        col = idx % 3
        col_count = [self.board[col+i*3] for i in range(3)]
        if all([s == letter for s in col_count]):
            return True
        
        if idx in [0, 2, 4, 6, 8]:
            # d1 = [self.board[i*4] for i in range(3)]
            # d2 = [self.board[i*2] for i in range(1, 4)]
            if all([self.board[i*4] == letter for i in range(3)]):
                return True
            
            elif all([self.board[i*2] == letter for i in range(1, 4)]):
                return True
        # print([self.board[i*4] for i in range(3)])
        # print([self.board[i*2] for i in range(1, 4)])
        return False
        # diagonal
    

def play(game, x_player, o_player):
        letter = 'X'
        
        while game.has_empty_squares():
            if letter == 'X':
                idx = x_player.get_move(game)
            else:
                idx = o_player.get_move(game)
            
            if game.make_move(letter, idx):
                game.print_board()
            if game.winner:
                print(f"The winner is: player {letter}!")
                return
            # print(idx, letter)
            letter = 'O' if letter == 'X' else 'X'
            # print(game.get_num_empty_squares())
        print('It\'s a tie')

        
game = TicTacToe()
x_player = HumanPlayer('X')
o_player = SmartComputerPlayer('O')
play(game, x_player, o_player)