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

    def printBoard(self):
        print('------')
        for i in self.board:
            line = ''
            for j in i:
                if j == 1:
                    line += 'X '
                elif j == -1:
                    line += 'O '
                else:
                    line += '_ '
            print(line)
            print('------')
    def makeAMove(self, move):
        #check if selected move is available

        if self.board[self.refchart(move[0])][int(move[1])-1]==0:
            #available
            self.board[move[0], move[1]]=self.current_player
            self.current_player *= -1
        else:
            print("Error: space not available")
            return 0
    def evaluateGame(self):
        return 'Not Done Yet'
            
        
