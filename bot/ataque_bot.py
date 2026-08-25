import random


def ataque_bot(tabuleiro_jogador, mostrar_tabuleiro):

    while True:

        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        casa = tabuleiro_jogador[linha][coluna]

        if casa == " N ":

            tabuleiro_jogador[linha][coluna] = " X "

            print("\nBOT ATACOU!")
            print("ACERTOU!")

            mostrar_tabuleiro(tabuleiro_jogador)

            return

        elif casa == " ~ ":

            tabuleiro_jogador[linha][coluna] = " O "

            print("\nBOT ATACOU!")
            print("ÁGUA!")

            mostrar_tabuleiro(tabuleiro_jogador)

            return