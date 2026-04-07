import random


def generate_number():
    return random.randint(1, 100)


def check_guess(secret, guess):
    if guess < secret:
        return "Too Low"
    elif guess > secret:
        return "Too High"
    else:
        return "Correct"


def play_game():
    number = generate_number()
    attempts = 0

    print("🎮 Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        result = check_guess(number, guess)
        print(result)

        if result == "Correct":
            print(f"You guessed it in {attempts} attempts!")
            break


if __name__ == "__main__":
    import os

    if os.getenv("CI"):
        print("Running in CI mode - skipping interactive game")
    else:
        play_game()
