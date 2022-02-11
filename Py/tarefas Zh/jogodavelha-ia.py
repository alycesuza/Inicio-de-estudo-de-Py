matriz = [["", "", ""], ["", "", ""], ["", "", ""]]


def computador():
    marcou = False
    for i in range(2):
        if ((matriz[1][i] == "X") and (matriz[2][i] == "X") and (matriz[0][i] != "O") and (matriz[0][i] != "X")):
            if (marcou == False):
                marcou = True
                entrada(i+1, "O")

    for i in range(2):
        if ((matriz[0][i] == "X") and (matriz[2][i] == "X") and (matriz[1][i] != "O") and (matriz[1][i] != "X")):
            if (marcou == False):
                marcou = True
                entrada(i+4, "O")

    for i in range(2):
        if ((matriz[0][i] == "X") and (matriz[1][i] == "X") and (matriz[2][i] != "O") and (matriz[2][i] != "X")):
            if (marcou == False):
                marcou = True
                entrada(i+7, "O")

    cont = 1
    for i in range(2):
        if ((matriz[i][1] == "X") and (matriz[i][2] == "X") and (matriz[i][0] != "O") and (matriz[i][0] != "X")):
            if (marcou == False):
                marcou = True
                entrada(cont, "O")
        cont += 3

    cont = 2
    for i in range(2):
        if ((matriz[i][0] == "X") and (matriz[i][2] == "X") and (matriz[i][1] != "O") and (matriz[i][1] != "X")):
            if (marcou == False):
                marcou = True
                entrada(cont, "O")
        cont += 3

    cont = 3
    for i in range(2):
        if ((matriz[i][0] == "X") and (matriz[i][1] == "X") and (matriz[i][2] != "O") and (matriz[i][2] != "X")):
            if (marcou == False):
                marcou = True
                entrada(cont, "O")
        cont += 3

    # cruzado
    if ((matriz[0][0] == "X") and (matriz[1][1] == "X") and (matriz[2][2] != "O") and (matriz[2][2] != "X")):
        if (marcou == False):
            marcou = True
            entrada(9, "O")
    elif ((matriz[0][2] == "X") and (matriz[1][1] == "X") and (matriz[2][0] != "O") and (matriz[2][0] != "X")):
        if (marcou == False):
            marcou = True
            entrada(7, "O")
    elif ((matriz[2][0] == "X") and (matriz[1][1] == "X") and (matriz[0][2] != "O") and (matriz[0][2] != "X")):
        if (marcou == False):
            marcou = True
            entrada(3, "O")
    elif ((matriz[2][2] == "X") and (matriz[1][1] == "X") and (matriz[0][0] != "O") and (matriz[0][0] != "X")):
        if (marcou == False):
            marcou = True
            entrada(1, "O")
    elif ((matriz[1][1] != "X") and (matriz[1][1] != "O")):
        if (marcou == False):
            marcou = True
            entrada(5, "O")
    elif ((matriz[1][0] != "X") and (matriz[1][0] != "O")):
        if (marcou == False):
            marcou = True
            entrada(4, "O")
    elif ((matriz[2][0] != "X") and (matriz[2][0] != "O")):
        if (marcou == False):
            marcou = True
            entrada(7, "O")
    elif ((matriz[0][2] != "X") and (matriz[0][2] != "O")):
        if (marcou == False):
            marcou = True
            entrada(3, "O")
    elif ((matriz[0][0] != "X") and (matriz[0][0] != "O")):
        if (marcou == False):
            marcou = True
            entrada(1, "O")
    elif ((matriz[2][2] != "X") and (matriz[2][2] != "O")):
        if (marcou == False):
            marcou = True
            entrada(9, "O")
    # ------


def entrada(posicao=0, marca=""):
    if (posicao == 1):
        matriz[0][0] = marca
    elif (posicao == 2):
        matriz[0][1] = marca
    elif (posicao == 3):
        matriz[0][2] = marca

    elif (posicao == 4):
        matriz[1][0] = marca
    elif (posicao == 5):
        matriz[1][1] = marca
    elif (posicao == 6):
        matriz[1][2] = marca

    elif (posicao == 7):
        matriz[2][0] = marca
    elif (posicao == 8):
        matriz[2][1] = marca
    elif (posicao == 9):
        matriz[2][2] = marca


def apresentar():
    print("\n")
    print("", matriz[0][0], "   |   ", matriz[0]
          [1], "   |   ", matriz[0][2], " ")
    print("--------------------")
    print("", matriz[1][0], "   |   ", matriz[1]
          [1], "   |   ", matriz[1][2], " ")
    print("--------------------")
    print("", matriz[2][0], "   |   ", matriz[2]
          [1], "   |   ", matriz[2][2], " ")
    print("\n")


def ganhou(g=""):
    if (((matriz[0][0] == g) and (matriz[0][1] == g) and (matriz[0][2] == g)) or ((matriz[1][0] == g) and (matriz[1][1] == g) and (matriz[1][2] == g)) or ((matriz[2][0] == g) and (matriz[2][1] == g) and (matriz[2][2] == g)) or ((matriz[0][0] == g) and (matriz[1][0] == g) and (matriz[2][0] == g)) or ((matriz[0][1] == g) and (matriz[1][1] == g) and (matriz[2][1] == g)) or ((matriz[0][2] == g) and (matriz[1][2] == g) and (matriz[2][2] == g)) or ((matriz[0][0] == g) and (matriz[1][1] == g) and (matriz[2][2] == g)) or ((matriz[2][0] == g) and (matriz[1][1] == g) and (matriz[0][2] == g))):
        print(g, "Ganhou! Parabéns <3")
        return True
    else:
        return False


def bemvindo():
    inicio = True
    while inicio:
        inicio = input(
            'Deseja iniciar o jogo? digite "S" para sim e "N" para Não: \n')
        if inicio == "S":
            print("Que vença o melhor ...")
            return TrueS
        else:
            print("Que pena, até a proxima!")
            exit()


jogada = False
cont = 1
jogadas = 0
uj = ""

for j in range(3):
    for i in range(3):
        matriz[j][i] = str(cont)
        cont += 1


def jogo():
    global jogada, cont, jogadas, uj, matriz
    try:

        numj = int(input('Quantos jogadores são? Digite "1" ou "2". '))
        if numj == 1:
            while True:

                apresentar()
                print(10 * "-=")
                if (jogada == False):
                    posicao = int(input("\n Digite a posição: "))
                    entrada(posicao, "X")
                    jogada = True
                    if (ganhou("X")):
                        apresentar()
                        break
                else:
                    computador()
                    if ganhou("O"):
                        apresentar()
                        break
                    jogada = False

                jogadas += 1
                if (jogadas == 9):
                    print("Deu velha")
                    break

        else:

            while True:
                apresentar()
                print(10 * "-=")
                if (jogada == False):
                    posicao = int(input("\n Digite a posição: "))
                    entrada(posicao, "X")
                    jogada = True
                    if (ganhou("X")):
                        apresentar()
                        break
                else:
                    posicao = int(input("\n Digite a posição: "))
                    entrada(posicao, "O")
                    jogada = False
                    if (ganhou("O")):
                        apresentar()
                        break

                jogadas += 1
                if (jogadas == 9):
                    print("Deu velha")
                    break

    except KeyboardInterrupt:
        print("........  Até a proxima ^^ ..........")
        exit()


if __name__ == "__main__":
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