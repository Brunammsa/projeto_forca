
def change_word_to_underline(word) -> str:
    return 'a'

def remove_special_characters(word) -> str:
    return 'a'

def check_if_exists_on_word(word, letter):
#   return letter in word
    if letter.lower() in word.lower():
        return True
    else:
        return False

def show_correct_letters(word, tries) -> str:

    return 'a'


def parse_input() -> str:
    
    answer = input("Por favor, digite a letra desejada: ")    
    
    while len(answer) == 0 or not answer.isalpha():
        answer = input("Resposta inválida. Por favor, digite a letra desejada: ")

    letter_lower = answer.lower()
    return letter_lower[0]
