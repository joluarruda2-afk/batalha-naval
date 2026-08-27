from ataque.ataque import abrir_ataque
from bot.tabuleiro_bot import preparar_bot
from bot.ataque_bot import ataque_bot


def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        if " N " in linha:
            return False

    return True


def iniciar_partida(tabuleiro_jogador, mostrar_tabuleiro):

    # Cria o tabuleiro do bot
    tabuleiro_bot = preparar_bot()

    while True:

        # =========================
        # VEZ DO JOGADOR
        # =========================

        print("\n===== SUA VEZ =====")

        abrir_ataque(tabuleiro_bot, mostrar_tabuleiro)

        if verificar_vitoria(tabuleiro_bot):
            print("\n======================")
            print("      VITÓRIA!")
            print("======================")
            break


        # =========================
        # VEZ DO BOT
        # =========================

        print("\n===== VEZ DO BOT =====")

        ataque_bot(tabuleiro_jogador, mostrar_tabuleiro)

        if verificar_vitoria(tabuleiro_jogador):
            print("\n======================")
            print("      DERROTA!")
            print("======================")
            break