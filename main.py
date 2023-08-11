import random

game_start_message = input('Press Enter to begin:')
while True:
    while game_start_message == "":
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        player_choice = None
        while player_choice not in choices:
            player_choice = input("choose: rock paper or scissors: ").lower()

        print("player choice: " + player_choice)
        print("computer choice: " + computer_choice)

        if player_choice == computer_choice:
            print("Tie")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print('Player wins!!')
            if computer_choice == "paper":
                print("computer wins")
        elif player_choice == "paper":
            if computer_choice == "scissors":
                print('computer wins!!')
            if computer_choice == "rock":
                print("player wins")
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print('computer wins!!')
            if computer_choice == "paper":
                print("computer wins")
        break
    play_again = input("Would you like to play again (yes/no)").lower()
    if play_again != "yes":
        break

print('bye')
