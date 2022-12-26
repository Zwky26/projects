from tictactoe import *
from ai import *
def play():
    g = game()
    print('Starting game: ' + ('(AI player goes first)' if g.ai_player == 1 else '(You go first)'))
    status = 1
    while status:
        if g.current_player == g.ai_player:
            #ai turn
            g.makeAMove(randomMove(g.availablemoves))
            eval = g.evaluateGame()
            if eval != 'Not Done Yet':
                g.printBoard()
                print(eval)
                status=0
        else:
            g.printBoard()
            nextMove = str(input("Enter your next move: "))
            g.makeAMove(nextMove)
            eval = g.evaluateGame()
            if eval != 'Not Done Yet':
                g.printBoard()
                print(eval)
                status=0

if __name__ == '__main__':
    while True:
        play()
        again = input('play again? (y/n): ')
        if again == 'n':
            break