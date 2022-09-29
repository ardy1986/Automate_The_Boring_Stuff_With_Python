import random, sys

print('ROCK, PAPER, SCISSORS')

# This variables keep track of the number of wins, losses, and ties.

wins = 0
losses = 0
ties = 0

# The main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    # The player input loop.
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
            sys.exit()      # quit the program.
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break           # Break out the player input loop.

        print('Type one of r, p, s, or q.')

    # Display what the player choose:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
    elif player_move == 'p':
        print('PAPER versus...')

    # Display what the computer choose:
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    if random_number == 2:
        computer_move = 'p'
        print('PAPER')
    if random_number == 3:
        computer_move = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        losses = losses + 1
