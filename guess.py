import random

def main():
    print("Welcome to the Number Guessing Game!")
    name = input("What's your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")
    play_game()

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess == number_to_guess:
            print(f"Congratulations, you've guessed the number ({number_to_guess}) correctly in {attempts} attempts!")
            play_again()
            return
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}. Game over.")
    play_again()

def play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    main()
