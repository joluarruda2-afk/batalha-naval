from partida.partida import iniciar_partida

import time
def abrir_tabuleiro():
        while True:
#escolhe as classes disponiveis.
                frota = input("""
[1] Porta-avião
* Ocupa 4 espaço

[2] Cruzador
* Ocupa 3 espaço

[3] Submarino
* Ocupa 2 espaço\n>>""")

                if frota == '1':
                        time.sleep(1)
                        print("Você escolheu a frota Porta-avião :)\n")
                        tamanho_navio = 4
                        break
                elif frota == '2':
                        time.sleep(1)
                        print("Você escolheu a frota Cruzador :)\n")
                        tamanho_navio = 3
                        break
                elif frota == '3':
                        time.sleep(1)
                        print("Você escolheu a frota Submarino :)\n")
                        tamanho_navio = 2
                        break
                else:
                        print("opção errada\n")

        
               

                
        tamanho = 10
        tabuleiro = []

        for i in range(tamanho):
                linha = [" ~ "] * tamanho
                tabuleiro.append(linha)

        def mostrar_tabuleiro(tab):
                print("   A   B   C   D   E   F   G   H   I   J")

                for indice, linha in enumerate(tab):
                 print(indice, " ".join(linha))

        mostrar_tabuleiro(tabuleiro)
        

        posicao = input("\nEscolha a posição pra colocar sua frota : ")
        colunas = posicao[0]
        linhas = posicao[1]

        direcao = input("\nEscolha a direção (horizontal ou vertical): ")

        print("\ncolunas", colunas)
        print("linhas", linhas)

        colunas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

        colunas = colunas.index(posicao[0].upper())
        linhas = int(posicao[1:])
        if direcao == 'horizontal':
                for i in range(tamanho_navio):
                        tabuleiro[linhas][colunas + i] = (" N ")
        elif direcao == 'vertical':
                for i in range(tamanho_navio):
                        tabuleiro[linhas + i][colunas] = (" N ")
        else:
                print("opção errada")

        mostrar_tabuleiro(tabuleiro)

        from partida.partida import iniciar_partida

        iniciar_partida(tabuleiro, mostrar_tabuleiro)
        