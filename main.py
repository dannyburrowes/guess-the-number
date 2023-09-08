import random

print("Welcome to Guess the Number!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
guess = 0
guesses_remaining = 10
game_over = False


def play():
    global guess
    guess = int(input("Make a guess: "))


def check_guess():
    global game_over
    if guess == number:
        game_over = True
        print(f"You guessed right! The number was {number}.")
    elif guess != number:
        global guesses_remaining
        guesses_remaining -= 1
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        if guesses_remaining > 0:
            print("Guess again.")
        if guesses_remaining == 1:
            print(f"You have {guesses_remaining} guess remaining.")
        if guesses_remaining > 1:
            print(f"You have {guesses_remaining} guesses remaining.")


if difficulty == "easy":
    print("You have 7 attempts to guess the number.")
    guesses_remaining = 7
elif difficulty == "hard":
    print("You have 5 attempts to guess the number.")
    guesses_remaining = 5

while guesses_remaining > 0 and not game_over:
    play()
    check_guess()

if guesses_remaining == 0:
    print("Game over.")
    print(f"The correct answer was {number}.")