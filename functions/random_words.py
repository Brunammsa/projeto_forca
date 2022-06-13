from random import choice

def get_random_name():

    arquivo = open('C:\\Users\\Haru\\Desktop\\projeto_01_forca\\files\\words.txt', 'r')
    lista_de_palavras = []

    for linha in arquivo:
        linha = linha.rstrip()
        lista_de_palavras.append(linha)

    arquivo.close()

    return choice(lista_de_palavras)
