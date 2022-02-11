#Python - Aula01 | At.01 ( Jogo da velha) - Bot burro

matriz = True


def bemvindo():
    inicio = True
    while inicio:
        inicio = input(
            'Deseja iniciar o jogo? digite "S" para sim e "N" para Não: \n')
        if inicio == "S":
            print("Que vença o melhor ...")
            jogo()
        else:
            print("Que pena, até a proxima!")
            break


def bot():
    for i in range(3):
        for j in range(3):
            if matriz[i][j].isdigit():
                return matriz[i][j]


def jogo():

    global matriz

    tabuleiro = '''
      {} |  {}  |  {}
    ____|_____|_____
      {} |  {}  |  {}
    ____|_____|_____
      {} |  {}  |  {}
        |     |
    '''

    def genMatriz():
        MTR = [['0', '1', '2'],
               ['3', '4', '5'],
               ['6', '7', '8']]
        return MTR

    def ganhou(char):

        for i in range(3):

            if matriz[i].count(char) == 3:
                return True
            elif matriz[0][i] == matriz[1][i] == matriz[2][i] == char:
                return True

        if matriz[0][0] == matriz[1][1] == matriz[2][2] == char:
            return True
        elif matriz[0][2] == matriz[1][1] == matriz[2][0] == char:
            return True

        return False

    def setElement(tmp):
        global matriz

        for i in range(3):
            for j in range(3):
                if matriz[i][j] == tmp[0]:
                    if matriz[i][j].isdigit():
                        matriz[i][j] = tmp[1]
                        return True
                    else:
                        return False

    matriz = genMatriz()

    print(tabuleiro.format(*matriz[0], *matriz[1], *matriz[2]))

    uj = ""
    try:
        numj = input('Quantos jogadores são? Digite "1" ou "2". ')
        if numj == 2:
            for i in range(9):

                jogador = input('Digite a inicial do seu nome: ')
                jogada = input('Digite a posição da sua jogada: ')

                while uj == jogador:
                    print('Sem trapaça, não é sua vez!')
                    jogador = input('Digite a inicial do seu nome: ')
                    jogada = input('Digite a posição da sua jogada: ')

                if setElement([jogada, jogador]):
                    uj = jogador

                    print(tabuleiro.format(*matriz[0], *matriz[1], *matriz[2]))

                    if ganhou(jogador):
                        print('o {} ganhou!'.format(jogador))
                        matriz = genMatriz()
                        break
                else:
                    print('digita certo filho da puta!')

            print('Deu velha')

        else:
            for i in range(9):
                cal = i % 2

                if cal == 0:
                    print('\n Sua vez, você é o "X" \n')
                    jogador = "X"
                    jogada = input('Digite a posição da sua jogada: ')

                else:
                    jogador = "O"
                    jogada = bot()

                if setElement([jogada, jogador]):
                    print(tabuleiro.format(*matriz[0], *matriz[1], *matriz[2]))

                    if ganhou(jogador):
                        print('o {} ganhou!'.format(jogador))
                        matriz = genMatriz()
                        break
                else:
                    print('digita certo filho da puta!')

                print('Empate!! \n')

    except KeyboardInterrupt:
        exit()


bemvindo()