# Abby H- wordle 3/18/2023

# importing colored text
from colorama import Back, Style
import random

WORD_LENGTH = 5

# list of letters that aren't in word
bad_letters = []

# word to guess
hidden_word = ""


# set the hidden word randomly
def load_hidden_word():

    # declare hidden word as global so we can set it
    global hidden_word

    # opens dictionary file
    with open(r'/Users/abbyhiggins/Desktop/family.txt', 'r') as fp:
        wordlist = fp.read()

    # breaks file into list, new item every new line of file
    data_into_list = wordlist.split("\n")

    # chooses random word from list
    hidden_word = str(random.choice(data_into_list)).upper()


# function to ask for a word and checks if its 5 letters
def get_guess():
    while True:
        guess_word = input().upper()
        if len(guess_word) == WORD_LENGTH:
            break
        else:
            print("Guess must be 5 letters ")
    return guess_word


# check word and print colored response
# return 1 = right answer, 0 wrong answer
def check_word(guess_word):

    # is the word the exact word?
    if guess_word == hidden_word:
        # prints the word in green, and finishes
        print(Back.GREEN + guess_word, end='')
        print(Style.RESET_ALL, "Great Job!")
        return 1

    # for loop to compare letters with guess
    for i in range(WORD_LENGTH):

        # if letter at same position matches, print green
        if hidden_word[i] == guess_word[i]:
            print(Back.GREEN + guess_word[i], end='')
        else:
            # if letter at different position matches, print yellow
            letter_to_find = guess_word[i]
            if hidden_word.find(letter_to_find) > 0:
                print(Back.YELLOW + letter_to_find, end='')
            else:
                # if letter doesn't match, print red and add to incorrect letter list, if letter isn't already in list
                print(Back.RED + letter_to_find, end='')
                if bad_letters.count(letter_to_find) == 0:
                    bad_letters.append(letter_to_find)

    # end color and print bad letters on same line
    print(Style.RESET_ALL, end='     ')
    display_bad_letters()

    # didn't guess the word
    return 0


# showing the letters that do not work
def display_bad_letters():
    bad_letters.sort()

    bad_letters_message = "Bad letters: ["

    # add letters from bad letter list and add a comma
    for letter in bad_letters:
        bad_letters_message += letter + ","

    # get rid of last comma
    bad_letters_message = bad_letters_message[0:(len(bad_letters_message)-1)] + "]"

    print(bad_letters_message)


# main game loop
def main():
    load_hidden_word()

    # limits amount of tries, tells actual word
    print('Enter your guess: ', end='')
    for i in range(6):
        word = get_guess()
        if check_word(word) == 1:
            break
    else:
        print("You lose! "+"The word was: " + hidden_word)


main()


