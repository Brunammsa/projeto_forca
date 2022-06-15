from random import choice

def get_random_name():

    arch = open('C:\\Users\\Haru\\Desktop\\projeto_01_forca\\files\\words.txt', 'r')
    words_list = []

    for line in arch:
        line = line.rstrip()
        words_list.append(line)

    arch.close()

    aux_empty = len(words_list)
    if aux_empty == 0:
        raise ValueError ("pasta de palavras esta vazia")

    return choice(words_list)
