def game_start():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~ BEM VINDO AO JOGO DA FORCA ~~~~~~~~~~~~~~~~~~~~~~~~~\nO tema é: Frutas!\nRegras do jogo:\n- Apenas palavras em letras minúsculas;\n- Sem caracteres especiais;\n- Sem acentos;\n- Você irá iniciar o jogo com 6 vidas;")


def you_lost():
    print("Que pena, não foi dessa vez!")


def you_won():
    print("Parabéns, você desvendou a palavra secreta!")


def reveal_secret_word(word):

    word = get_random_name()

    print("Esta é a palavra secreta: {}".format(word))


def doesnt_exists(letter):
    print("Esta letra não existe na palavra, tente novamente com outra!")

def users_life(life):

    sum_tries = 0
    lifes = 6

    while sum_tries < lifes:
        if doesnt_exists(letter):
            sum_tries += 1
            return "Você ainda tem {} vidas!".format(lifes-sum_tries)
        if sum_tries == lifes:
            return you_lost()
            

def letters_tried(letters):

    letters = letters_tried(letters)

    print("Tentativas: {}".format(letters))
