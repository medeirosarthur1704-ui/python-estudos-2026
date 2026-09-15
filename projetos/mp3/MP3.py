# ================================================================
# MP3 PLAYER
# Player de áudio de terminal: carrega um arquivo de música e
# permite pausar, retomar e parar a reprodução em tempo real,
# através de comandos digitados pelo usuário.
# ================================================================

import pygame                 # biblioteca externa usada pelo módulo de áudio (mixer)
import pyfiglet               # gera o banner em ASCII art
from time import sleep        # cria pausas (efeito de "processando")

try:

    # Banner de título, em vermelho
    banner = pyfiglet.figlet_format("MP3 Player", font="slant")
    print(f"\033[1;38;2;255;0;0m{banner}\n")

    # Inicializa o subsistema de áudio do pygame — precisa rodar antes de tocar qualquer som
    pygame.mixer.init()

    # Pede o caminho/nome do arquivo de música que o usuário quer tocar
    nome_arquivo = input("\033[1;33m\n[+] Informe o nome do arquivo de música: ")

    # Carrega o arquivo de áudio na memória
    pygame.mixer.music.load(nome_arquivo)
    print("\033[1;32m[+] Reproduzindo música...")
    sleep(2)  # pausa só pra dar a sensação de "processamento"

    # Começa a tocar a música carregada
    pygame.mixer.music.play()
    print("\033[1;32mMúsica em reprodução. Use os comandos abaixo para controlar a reprodução.")


    while True:

        # Loop de comandos: fica esperando o usuário digitar uma ação
        comando = input(
            "\033[1;36mDigite [P] para pausar, [C] para continuar ou [S] para sair: "
        ).strip().upper()

        if comando == "P":
            pygame.mixer.music.pause()   # pausa a música sem perder a posição
            print("\033[1;33mMúsica pausada.")

        elif comando == "C":
            pygame.mixer.music.unpause()  # retoma de onde parou
            print("\033[1;32mReprodução continuada.")

        elif comando == "S":
            pygame.mixer.music.stop()    # para a reprodução por completo
            print("\033[1;35mReprodução encerrada.")
            break                        # sai do while True, encerrando o programa

        else:
            print("\033[1;31mComando inválido. Tente novamente.")


# pygame.error cobre falhas como arquivo inexistente, formato não suportado, etc.
except pygame.error:
    print("\033[1;31mErro: não foi possível carregar ou reproduzir o arquivo de música.")
except KeyboardInterrupt:
    # Se o usuário apertar Ctrl+C a qualquer momento dentro do try 
    print("\n\033[1;31m[-] Processo interrompido pelo usuário.")