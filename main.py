from functions.outputs import game_start
from functions import random_words
from functions.helpers import remove_special_characters
from functions.helpers import change_word_to_underline
from functions.helpers import parse_input
from functions.helpers import check_if_exists_on_word


game_start()
secret_word = random_words.get_random_name()
word_clean = helpers.remove_special_characters(secret_word)
words_in_underline = helpers.change_word_to_underline(word_clean)
parse_input()

life = 6
hanged = False
winner = False
tries = []
incorrect_tries = []

while not hanged and not winner:

    letter_try = parse_input()
    letters_word = check_if_exists_on_word(word_clean, letter_try)

    if letter_try in tries:
        print("You already tried this letter, please try another one: ")
        letter_try

    if letter_try not in letters_word:
        outputs.doesnt_exists
        life -= 1
        letter_try.append(incorrect_tries)
        letter_try.append(tries)
        outputs.users_life(life)
        outputs.letters_tried(incorrect_tries)
        if life == 0:
            hanged = True

    if letter_try in letters_word:
        letter_try.append(tries)
        helpers.show_correct_letters(word_clean, letter_try)

if winner == True:
    outputs.you_won

if hanged == True:
    outputs.you_lost
    outputs.reveal_secret_word