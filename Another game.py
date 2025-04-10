# Guess the Number Game (Mini Python Project)
# Computer ek random number choose karega (1 se 10 ke beech)
# User usse guess karega
# Agar sahi guess kiya → 🎉 "You won!"
# Galat guess → Hint dega "Try again!"
# 3 baar galat guess → Game Over ❌


import random

while True:
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n🎲 Welcome to the Guessing Game!")
    print("Guess a number between 1 and 10. You have 3 chances.\n")

    while attempts < 3:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("🎉 You guessed it right! You win!")
            break
        elif guess < secret_number:
            print("🔼 Too low! Try again.")
        else:
            print("🔽 Too high! Try again.")

    if guess != secret_number:
        print(f"😢 Game Over! The correct number was {secret_number}")

    # 🔁 Ask user if they want to play again
    play_again = input("\n🔁 Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("👋 Thanks for playing, Saloni! See you next time!")
        break

