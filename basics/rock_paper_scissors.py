import random

options = ("rock", "paper", "scissors")
running = True

while running:

    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors): ")
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "paper" and computer == "rock":
        print("You won")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("You lose!")

    if input("Wanna play again? (y/n)").lower() == 'y':
        running = True
    else:
        running = False
        print("Thank you for Playing!")

    