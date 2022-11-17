def game_start():
    print(
        '~~~~~~~~~~~~~~~~~~~~~~~~~ BEM VINDO AO JOGO DA FORCA ~~~~~~~~~~~~~~~~~~~~~~~~~\nO tema é: Frutas!\nRegras do jogo:\n- Apenas palavras em letras minúsculas;\n- Sem caracteres especiais;\n- Sem acentos;\n- Você irá iniciar o jogo com 6 vidas;'
    )


def you_lost():
    print('Que pena, não foi dessa vez!')


def you_won():
    print('Parabéns, você desvendou a palavra secreta!')


def reveal_secret_word(word):

    word = get_random_name()

    print('Esta é a palavra secreta: {}'.format(word))


def doesnt_exists(letter):
    print('Esta letra não existe na palavra, tente novamente com outra!')


def users_life(life):

    if life == 0:
        you_lost()
    else:
        print(f'Você ainda tem {life} vidas')


def letters_tried(letters):

    print(f'Tentativas: {letters}')
