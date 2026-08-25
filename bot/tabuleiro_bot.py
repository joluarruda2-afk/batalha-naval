import random


def criar_tabuleiro_bot():

    tabuleiro = []

    for linhas in range(10):
        linha = []

        for colunas in range(10):
            linha.append(" ~ ")

        tabuleiro.append(linha)

    return tabuleiro


def colocar_navio_bot(tabuleiro):

    tamanho_navio = 4

    while True:

        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        direcao = random.choice([
            "horizontal",
            "vertical"
        ])

        if direcao == "horizontal":

            if coluna + tamanho_navio <= 10:

                for i in range(tamanho_navio):
                    tabuleiro[linha][coluna + i] = " N "

                break

        else:

            if linha + tamanho_navio <= 10:

                for i in range(tamanho_navio):
                    tabuleiro[linha + i][coluna] = " N "

                break


def preparar_bot():

    tabuleiro = criar_tabuleiro_bot()

    colocar_navio_bot(tabuleiro)

    return tabuleiro