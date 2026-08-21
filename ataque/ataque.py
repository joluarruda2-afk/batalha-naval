def abrir_ataque(tabuleiro_inimigo, mostrar_tabuleiro):

    ataque = input("Qual lugar você quer atacar? ")

    colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    coluna = colunas.index(ataque[0].upper())
    linha = int(ataque[1:])

    mostrar_tabuleiro(tabuleiro_inimigo)

    if tabuleiro_inimigo[linha][coluna] == " N ":
        print("ACERTOU!")
        tabuleiro_inimigo[linha][coluna] = " X "

    else:
        print("ÁGUA!")
        tabuleiro_inimigo[linha][coluna] = " O "

    