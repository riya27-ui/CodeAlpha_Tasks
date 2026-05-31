import random

words = ["tiger", "pizza", "apple", "beach", "chair"]

word = random.choice(words)

guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman Game 🎮")
print("Guess the word one letter at a time!\n")

while tries > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", guessed_letters)
    print("Tries Left:", tries)

    if "_" not in display_word:
        print("\nYAY!!! Congratulations! You won!🎉")
        break

    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print("⚠ You already guessed that letter!")

    elif guess in word:
        print("✅ Correct Guess!")
        guessed_letters.append(guess)

    else:
        print("❌ Wrong Guess!")
        guessed_letters.append(guess)
        tries -= 1

if tries == 0:
    print("\n OH NO!! Game Over!")
    print("The word was:", word, "\n better luck next time!!")