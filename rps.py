#rps
import random

playermove = ['rock', 'paper', 'scissors']

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
        print('You Win!')
    elif move == 'paper' and comp_move == 'rock':
        print('You Win!')          
    elif move == 'scissors' and comp_move == 'paper':
        print('You Win!')
        
    elif move == 'rock' and comp_move == 'paper':
        print('Computer Wins!')
    elif move == 'paper' and comp_move == 'scissors':
        print('Computer Wins!')
    elif move == 'scissors' and comp_move == 'rock':
        print('Computer Wins!')

    print(' ')

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
