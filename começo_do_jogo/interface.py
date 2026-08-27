import time
from tabuleiro.tabuleiro import abrir_tabuleiro

# interface do jogo
print(r"""
                |    |____| |____,
          ______|_________________\________________
          \                                         /
           \             BATALHA NAVAL             /
~~~~~~~~~~~~\_____________________________________/~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
time.sleep(2)
print("---------------------------------------------\n")
# mostrar o texto
print("BEM-VINDO AO JOGO BATALHA NAVAL.\n")
time.sleep(1)
print("\n---------------------------------------------")


# isso e as regras do jogo com uma condição se ele quiser ver as regras ou não 
while True:
    regras = input("Você quer conhecer as regras?\nsim ou não \n>>")

    if regras == 'sim':
        print("""Cada jogador tem um tabuleiro, normalmente 10×10.
Cada jogador posiciona seus navios no próprio tabuleiro.
Os navios ocupam várias casas. Exemplo:
Porta-avião → 4 casas
Cruzador → 3 casas
Submarino → 2 casas
Os navios podem ficar na horizontal ou vertical, mas não na diagonal.
Os jogadores se revezam dando uma coordenada para atacar, por exemplo B5.
Se houver um navio naquela posição → acertou.
Se não houver → água/erro.
Quando todas as casas de um navio forem atingidas, ele é afundado.
Ganha quem afundar todos os navios do adversário primeiro.\n""")
        break
    elif regras == 'não':
        print("carregando..")
        time.sleep(2)
        break
    else:
        print("opção errada")
print("--------------------------------------------------\n")
nome = input("Escolha o nome de jogador?  ")
print("\n--------------------------------------------------")

print("então vamos lá" nome)
# E uma repetição pra alguem fazer uma opção errada ele repete 
while True:

    # É uma condição se ele quer continuar ou não
    decisao = input("[1] - jogar uma partida ;)\n[2] - sair\n")
 
    if decisao == '1':
        print("-------------------------\n")
        print("começando uma partida")
        print("\n-------------------------")
        time.sleep(1)
        abrir_tabuleiro()
        break
    elif decisao == '2':
        print("----------------------\n")
        print("saindo...")
        print("\n----------------------")
        time.sleep(2)
        break
    else:
        print("----------------------\n")
        print("opção errada")
        print("\n----------------------")