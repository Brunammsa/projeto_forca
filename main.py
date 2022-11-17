from functions.outputs import *
from functions import random_words
from functions.helpers import *


game_start()
secret_word = random_words.get_random_name()
word_cleaned = remove_special_characters(secret_word)
print(f'\nA palavra sorteada é a: {change_word_to_underline(word_cleaned)}\n')

life = 6
hanged = False
winner = False
tries = []
incorrect_tries = []

while not hanged and not winner:

    letter_try = parse_input()
    letter_try = remove_special_characters(letter_try)
    letters_word = check_if_exists_on_word(word_cleaned, letter_try)

    if letter_try in tries:

        print('Você já tentou esta letra, por favor tente uma outra.')

    elif letters_word:
        tries.append(letter_try)
        correct_letters = show_correct_letters(secret_word, tries)
        print(correct_letters)

        if '_' not in correct_letters:
            winner = True

    else:
        doesnt_exists(letter_try)
        life -= 1
        incorrect_tries.append(letter_try)
        tries.append(letter_try)
        users_life(life)
        letters_tried(incorrect_tries)
        if life == 0:
            hanged = True

if winner == True:
    you_won()

if hanged == True:
    you_lost()
    reveal_secret_word()
