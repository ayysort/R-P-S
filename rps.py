#rps
import random
win = 0
lose = 0
playermove = ['rock', 'paper', 'scissors']

# record keeping
def youwin():
    print("You Win!")
    global win
    win += 1
    
def youlose():
    print('Computer Wins!')
    global lose
    lose += 1
    
print(' ')
print(' ')
print(' ')
print('Welcome to Rock, Paper, Scissors!')

while True:
# input player move
    while True:
        print(' ')
        move = input('Enter your choice (Rock, Paper, Scissors): ').lower()
        if move in playermove:
            break
        else:
            print('Wrong Input...')
            continue

# computer move
    comp_move = random.choice(['rock', 'paper', 'scissors'])


# display moves
    print(' ')
    print(' ')
    print("You played", move.capitalize())
    print('Computer played', comp_move.capitalize())
    print(' ')

# compare moves
    if move == comp_move:
        print("It's a tie!")

    elif move == 'rock' and comp_move == 'scissors':
        youwin()
    elif move == 'paper' and comp_move == 'rock':
        youwin()          
    elif move == 'scissors' and comp_move == 'paper':
        youwin()
        
    elif move == 'rock' and comp_move == 'paper':
        youlose()
    elif move == 'paper' and comp_move == 'scissors':
        youlose()
    elif move == 'scissors' and comp_move == 'rock':
        youlose()

    print(' ')
    print('Your record is: ', win, '-', lose )

# play again?
    while True:
        again = input("Do you want to play again? (y/n): ")
        if again == 'y':
            break
        elif again == 'n':
            print(' ')
            print('Thanks for playing!')
            print(' ')
            exit()
        else:
            print("Wrong Input...")
