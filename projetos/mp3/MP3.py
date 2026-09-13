import pygame

try:
    pygame.mixer.init()

    nome_arquivo = input("Informe o nome do arquivo de música: ")

    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.play()

    while True:
        comando = input(
            "Digite [P] para pausar, [C] para continuar ou [S] para sair: "
        ).strip().upper()

        if comando == "P":
            pygame.mixer.music.pause()
            print("Música pausada.")

        elif comando == "C":
            pygame.mixer.music.unpause()
            print("Reprodução continuada.")

        elif comando == "S":
            pygame.mixer.music.stop()
            print("Reprodução encerrada.")
            break

        else:
            print("Comando inválido. Tente novamente.")

except pygame.error:
    print("Erro: não foi possível carregar ou reproduzir o arquivo de música.")