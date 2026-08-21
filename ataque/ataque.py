def abrir_ataque(tabuleiro_inimigo, mostrar_tabuleiro):
    print("----------------------------------------------------------------\n")
    ataque = input("Qual lugar você quer atacar? ")
    print("\n-----------------------------------------------------------------")
    colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    coluna = colunas.index(ataque[0].upper())
    linha = int(ataque[1:])

    if tabuleiro_inimigo[linha][coluna] == " N ":
        tabuleiro_inimigo[linha][coluna] = " X "
        print()
        mostrar_tabuleiro(tabuleiro_inimigo)
        print("ACERTOU!")

    else:
        print()
        tabuleiro_inimigo[linha][coluna] = " O "
        mostrar_tabuleiro(tabuleiro_inimigo)
        print("ÁGUA!")

    