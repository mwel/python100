# A variation of the hangman game for command line

import random
import words
import stages

word_list   =   words.word_list
alphabet    =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_used=   []
dead        =   False
chosen_word =   ""
blanks      =   ['_']
hangman     =   []
max_health  =   6
health      =   max_health


# game launch
def start_game():
    start = input("Would you like to start the game? Y/N")
    if start == "Y":
        print(stages.logo)
        chosen_word = random.choice(word_list)
        # print(f"CHEAT/CHECK: {chosen_word}")
        return chosen_word
    else:
        print("Ok. Bye.")
        quit()


def display_blanks(string):
    blanks = []
    for _ in chosen_word:
        blanks += "_"
    # blanks = ['_']*len(string)
    print(f"Guess the following word: \n\n {blanks}")
    return blanks


#check if the letter was already used
def checkIfUsed(char):
    if char in letters_used:
        print("Letter already in use. Please choose another.")
        return True
    else:
        letters_used.append(char)
        print(f"Letter available. Used letters: {letters_used}")
        return False


#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def containsLetter(string, char):
    if char in string:
        #print ("HIT")
        #replace blanks with respective letters
        for pos in range(len(chosen_word)):            
            letter = chosen_word[pos]
            if letter == char:
                blanks[pos] = char
        print(blanks)
        return True
    else:
        #print ("MISS")
        return False
    



def move(health):
    letter = input("Guess a letter!").lower()
    if checkIfUsed(letter):
        return health
    if containsLetter(chosen_word, letter):
        return health
    else:
        health -= 1
        print(f"Health Points: {health}")
    return health

def display_hangman(stage):
    print(stages.stages[stage])

def complete():
    if "_" not in blanks:
        print (f"You win! The word was {chosen_word}.")
        quit()
    else:
        return False


# main
chosen_word = start_game()
blanks = display_blanks(chosen_word)
word_as_list = list(chosen_word)
while not complete() and health > 0:
    health = move(health)
    stage = max_health - health
    display_hangman(stage)

print("Game Over.")
print(f"The correct word would have been {chosen_word}.")
