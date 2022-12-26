import random
class game:
    #definition of a tictactoe game
    refchart = {'a': 0, 'b': 1, 'c':2}
    def __init__(self):
        self.board = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]  
                    ]
        self.current_player = 1
        self.player1history = {'a':0, 'b':0, 'c':0, '1':0, '2':0, '3':0}
        self.player2history = {'a':0, 'b':0, 'c':0, '1':0, '2':0, '3':0}
        self.ai_player = -1 + (2 * random.randint(0, 1))
        self.availablemoves = []
        for i in ['a', 'b', 'c']:
            for j in ['1', '2', '3']:
                self.availablemoves.append (i+j)

    def printBoard(self):
        print('    A   B   C  ')
        print('  +---+---+---+')
        for rownum, i in enumerate(self.board):
            line = str(rownum + 1) + ' |'
            for j in i:
                if j == 1:
                    line += ' X |'
                elif j == -1:
                    line += ' O |'
                else:
                    line += '   |'
            print(line)
            print('  +---+---+---+')
    def makeAMove(self, move):
        #check if selected move is available

        if self.board[int(move[1])-1][self.refchart[move[0]]]==0:
            #available
            self.board[int(move[1])-1][self.refchart[move[0]]]=self.current_player
            if self.current_player == 1:
                self.player1history[move[0]] += 1
                self.player1history[move[1]] += 1
            else:
                self.player2history[move[0]] += 1
                self.player2history[move[1]] += 1
            self.current_player *= -1
            self.availablemoves.remove(move)
        else:
            print("Error: space not available")
            return 1
    def evaluateGame(self):
        if 3 in self.player1history.values():
            return 'Player 1 wins'
        elif 3 in self.player2history.values():
            return 'Player 2 wins'
        else:
            if (self.board[0][0], self.board[1][1], self.board[2][2]) == (1,1,1):
                return 'Player 1 wins'
            elif (self.board[0][0], self.board[1][1], self.board[2][2]) == (-1,-1,-1):
                return 'Player 2 wins'
            elif (self.board[0][2], self.board[1][1], self.board[2][0]) == (-1,-1,-1):
                return 'Player 2 wins'
            elif (self.board[0][2], self.board[1][1], self.board[2][0]) == (1,1,1):
                return 'Player 1 wins'
            return 'Not Done Yet'
            
        
