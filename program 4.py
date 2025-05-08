import random

def get_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock-Paper-Scissors ---")
        user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()

        if user == 'exit':
            print("Thanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Try again.")
            continue

        computer = get_choice()
        print(f"Computer chose: {computer}")
        result = get_winner(user, computer)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

play_game()
