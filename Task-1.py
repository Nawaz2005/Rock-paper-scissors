import random

def rock_paper_scissors():
    choices = ["Rock", "Paper", "Scissors"]
    
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: Rock, Paper, or Scissors.")

    while True:
        player_choice = input("Your choice: ").capitalize()
        if player_choice not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)
        print("Computer's choice:", computer_choice)

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Scissors" and computer_choice == "Paper") or \
             (player_choice == "Paper" and computer_choice == "Rock"):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing Rock, Paper, Scissors!")

rock_paper_scissors()
