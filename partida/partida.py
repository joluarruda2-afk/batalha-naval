from ataque.ataque import abrir_ataque
from bot.tabuleiro_bot import preparar_bot
from bot.ataque_bot import ataque_bot


def mostrar_tabuleiro_bot(tabuleiro):
    print("   A   B   C   D   E   F   G   H   I   J")

    for indice, linha in enumerate(tabuleiro):
        linha_escondida = []

        for casa in linha:
            if casa == " N ":
                linha_escondida.append(" ~ ")
            else:
                linha_escondida.append(casa)

        print(indice, " ".join(linha_escondida))


def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        if " N " in linha:
            return False

    return True


def iniciar_partida(tabuleiro_jogador, mostrar_tabuleiro):

    tabuleiro_bot = preparar_bot()

    while True:

        print("\n===== SUA VEZ =====")

        abrir_ataque(tabuleiro_bot, mostrar_tabuleiro_bot)

        if verificar_vitoria(tabuleiro_bot):
            print("\n======================")
            print("      VITÓRIA!")
            print("======================")
            break

        print("\n===== VEZ DO BOT =====")

        ataque_bot(tabuleiro_jogador, mostrar_tabuleiro)

        if verificar_vitoria(tabuleiro_jogador):
            print("\n======================")
            print("      DERROTA!")
            print("======================")
            break