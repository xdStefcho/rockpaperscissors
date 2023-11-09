from random import randint

player_wins = 0
computer_wins = 0
wining_score = 3
while player_wins < wining_score and computer_wins < wining_score:
    print(f'Player score : {player_wins} Computer score : {computer_wins}')
    print("..rock..")
    print("..paper..")
    print("..scissors")

    player = input("Enter your choice  ").lower()
    if player == quit or player == 'q':
        break
    random_num = randint(0, 2)
    if random_num == 0:
        computer = 'rock'
    elif random_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    print(f"The computer plays :{computer}")

    if player == computer:
        print('Its a tie ')
    elif player == 'rock':
        if computer != 'paper':
            print('Player wins!')
            player_wins += 1
        else:
            print('Computer wins!')
            computer_wins += 1
    elif player == 'paper':
        if computer == 'rock':
            print('Player wins!')
            player_wins += 1
        else:
            print('Computer wins!')
            computer_wins += 1from random import randint

def reset_scores():
    return 0, 0

def play_game():
    player_wins, computer_wins = reset_scores()
    winning_score = 3
    while True:
        if player_wins >= winning_score or computer_wins >= winning_score:
            break
        print(f'Player score: {player_wins} Computer score: {computer_wins}')
        print("..rock..")
        print("..paper..")
        print("..scissors")

        player = input("Enter your choice: ").lower()
        if player == 'quit' or player == 'q':
            continue
        random_num = randint(0, 2)
        if random_num == 0:
            computer = 'rock'
        elif random_num == 1:
            computer = 'paper'
        else:
            computer = 'scissors'
        print(f"The computer plays: {computer}")

        if player == computer:
            print('It\'s a tie ')
        elif player == 'rock':
            if computer == 'scissors':
                print('Player wins!')
                player_wins += 1
            else:
                print('Computer wins!')
                computer_wins += 1
        elif player == 'paper':
            if computer == 'rock':
                print('Player wins!')
                player_wins += 1
            else:
                print('Computer wins!')
                computer_wins += 1
        elif player == 'scissors':
            if computer == 'rock':
                print('Computer wins')
                computer_wins += 1
            else:
                print('Player wins!')
                player_wins += 1
        else:
            print('Enter a valid move!')

    if player_wins > computer_wins:
        print(f'CONGRATS YOU WON: {player_wins} wins')
    elif player_wins == computer_wins:
        print('THE GAME IS DRAW')
    else:
        print(f'UNFORTUNATELY COMPUTER WON: {computer_wins} wins')

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()

play_game()

    elif computer == 'rock':
        if player == 'scissors':
            print('Computer wins')
            computer_wins += 1
        else:
            print('Player wins!')
            player_wins += 1
    else:
        print('Enter a valid move!')
if player_wins > computer_wins:
    print(f'CONGRATS YOU WON : {player_wins} wins')
elif player_wins == computer_wins:
    print('THE GAME IS DRAW')
else:
    print(f'UNFORTUNATELY COMPUTER WON : {computer_wins} wins')
