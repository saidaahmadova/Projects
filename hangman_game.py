import random

words = ["python", "developer", "backend", "github", "computer"]

chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
lives = 6

print("Welcome to Hangman Game!")

while "_" in display and lives > 0:
    print("\nWord:", " ".join(display))
    print(f"Lives: {lives}")

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed this letter.")

    elif guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print("Correct!")

    else:
        lives -= 1
        print("Wrong guess.")

if "_" not in display:
    print("\nCongratulations! You won!")
    print("Word:", chosen_word)
else:
    print("\nGame Over.")
    print("The word was:", chosen_word)