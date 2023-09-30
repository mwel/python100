import random

word_list = ["aardvark", "baboon", "camel", "park", "element", "informatics"]
letters_used = []
chosen_word = ""
blanks = []

# Function to start the game
def start_game():
    start = input("Would you like to start the game? (Y/N): ").strip().lower()
    if start == "y":
        chosen_word = random.choice(word_list)
        print(f"CHEAT/CHECK: {chosen_word}")
        return chosen_word
    else:
        print("Okay. Goodbye.")
        quit()

# Function to display blanks for the word
def display_blanks(word):
    return ['_' for _ in word]

# Function to check if a letter is already used
def check_if_used(char):
    if char in letters_used:
        print("Letter already used. Please choose another.")
        return True
    else:
        letters_used.append(char)
        print(f"Available letters: {' '.join(letters_used)}")
        return False

# Function to check if the letter is in the chosen word
def contains_letter(word, char):
    if char in word:
        print("HIT!")
        for i in range(len(word)):
            if word[i] == char:
                blanks[i] = char
        print(' '.join(blanks))
        return True
    else:
        print("MISS!")
        return False

# Function to handle game over
def game_over(word, blanks, health):
    if '_' not in blanks:
        print(f"Congratulations! You guessed the word: {word}")
        return True
    elif health <= 0:
        print(f"Game over! The word was: {word}")
        return True
    else:
        return False

# Function for player's move
def move(word, blanks, health):
    letter = input("Guess a letter: ").strip().lower()

    if len(letter) != 1 or letter not in 'abcdefghijklmnopqrstuvwxyz':
        print("Invalid input. Please enter a single letter.")
    elif check_if_used(letter):
        health -= 1
    else:
        contains_letter(word, letter)
    return letter

# Function to display the hangman
def display_hangman(stage):
    hangman_stages = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="
    ]
    print(hangman_stages[stage])

# Main game loop
chosen_word = start_game()
blanks = display_blanks(chosen_word)
health = 6  # Maximum health (number of hangman stages)
stage = 0    # Current hangman stage
while not game_over(chosen_word, blanks, health):
    letter = move(chosen_word, blanks, health)
    if not contains_letter(chosen_word, letter):
        stage += 1
        display_hangman(stage)
print("Game Over.")
