from tictactoe import *

def play():
    print('Starting game')
    g = game()
    status = 1
    while status:
        g.printBoard()
        nextMove = str(input("Enter your next move: "))
        g.makeAMove(nextMove)
        if g.evaluateGame() == 'Done':
            break

if __name__ == '__main__':
    while True:
        play()
        again = input('play again? (y/n): ')
        if again == 'n':
            break