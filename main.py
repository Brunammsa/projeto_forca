from functions.outputs import game_start
from functions import random_words
from functions.helpers import remove_special_characters
from functions.helpers import change_word_to_underline
from functions.helpers import parse_input
from functions.helpers import check_if_exists_on_word

game_start()
secret_word = random_words.get_random_name()
parse_input()

#Tentar o corpo do jogo a partir daqui

change_word_to_underline(word)
remove_special_characters(word)
check_if_exists_on_word(word, letter)
show_correct_letters