import random

def number_guessing_game():
    print("Welcome to the number guessing game!")
    print("I have chosen a number from 1 to 100")
    print("Choose your difficulty")
    print("(1)Easy - 10 guesses")
    print("(2)Medium - 7 guesses")
    print("(3)Hard - 5 guesses")

# Choose level

    max_attempts = 0
    while max_attempts == 0:
        difficulty = input("Enter 1, 2, or 3 for difficulty: ")
        if difficulty == "1":
            max_attempts = 10
            print("You chose Easy mode. You have 10 guesses. Good luck!")
        elif difficulty == "2":
            max_attempts = 7
            print("You chose Medium mode. You have 7 guesses. Good luck!")
        elif difficulty == "3":
            max_attempts = 5
            print("You chose Hard mode. You have 5 guesses. Good luck!")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# random number 1 - 100

    target_number = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1} / {max_attempts}. Guess a number: ")
        if not guess.isdigit():
            print("Enter a valid response")
            continue

        guess = int(guess)
        attempts += 1

        if guess < target_number:
            print("Too Low")
        elif guess > target_number:
            print("Too High")
        else:
            print(f"You guessed {target_number} correctly in {attempts} attempts! Congratulations!")
            break

    #if no more attempts remain
    if attempts == max_attempts and guess != target_number:
        print(f"Sorry, you used all attempts. The number was {target_number}")
        print("Better luck next time")

#start game

number_guessing_game()




