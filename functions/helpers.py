from random_words import get_random_name
from unidecode import unidecode
from outputs import doesnt_exists
from outputs import users_life

def change_word_to_underline(word) -> str:

    word = get_random_name()
    underline = " _"
    secret_word_underline = ''

    for letter in word:
        secret_word_underline += underline

    return secret_word_underline

def remove_special_characters(word) -> str:

    word = get_random_name()
    without_special_char = unidecode(word)

    return without_special_char

def check_if_exists_on_word(word, letter):
#   return letter in word
    word = get_random_name()
    letter = parse_input()

    if letter.lower() in word.lower():
        return show_correct_letters(word, tries)
    else:
        return users_life(life)

def show_correct_letters(word, tries) -> str:
    
    word = change_word_to_underline(word)
    tries = letters_tries

    for index, letter in enumerate(word):
        if tries[index] == word[index]:

            return secret_word_underline[index] == tries[index]


def parse_input() -> str:
    
    answer = input("Por favor, digite a letra desejada: ")    
    
    while len(answer) == 0 or not answer.isalpha():
        answer = input("Resposta inválida. Por favor, digite a letra desejada: ")

    letter_lower = answer.lower()
    letters_tries = []
    letters_tries.append(letter_lower[0])

    return letter_lower[0]
