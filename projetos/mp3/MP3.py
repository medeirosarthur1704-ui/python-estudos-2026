import pygame   # biblioteca externa usada aqui só pelo módulo de áudio (mixer)

try:

    # Inicializa o subsistema de áudio do pygame — precisa rodar antes de tocar qualquer som
    pygame.mixer.init()

    # Pede o caminho/nome do arquivo de música que o usuário quer tocar
    nome_arquivo = input("\033[1;33mInforme o nome do arquivo de música: ")

    # Carrega o arquivo de áudio na memória
    pygame.mixer.music.load(nome_arquivo)

    # Começa a tocar a música carregada
    pygame.mixer.music.play()
    print("\033[1;32mReproduzindo...")


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
            # Qualquer outra tecla cai aqui, e o loop volta a perguntar
            print("\033[1;31mComando inválido. Tente novamente.")


# pygame.error cobre falhas como arquivo inexistente, formato não suportado, etc.
except pygame.error:
    print("\033[1;31mErro: não foi possível carregar ou reproduzir o arquivo de música.")