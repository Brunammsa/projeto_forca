import unidecode

def change_word_to_underline(word) -> str:

    underline = " _"
    secret_word_underline = ''

    for letter in word:
        secret_word_underline += underline

    return secret_word_underline


def remove_special_characters(word) -> str:

    word_without_special_char = unidecode.unidecode(word)

    return word_without_special_char


def check_if_exists_on_word(word, letter):
#   return letter in word

    if letter in word:
        return True
    else:
        return False

def show_correct_letters(word, tries) -> str:

    for index, letter in enumerate(word):
        if tries[index] == letter:

            return 


def parse_input() -> str:
    
    answer = input("Por favor, digite a letra desejada: ")
    
    while len(answer) == 0 or not answer.isalpha():
        print('Resposta inválida')
        answer = input("Por favor, digite a letra desejada: ")

    letter_lower = answer.lower()
    letters_tries = []
    letters_tries.append(letter_lower[0])

    return letter_lower[0]
