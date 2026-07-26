import pygame

try:
    pygame.mixer.init()

    nome_arquivo = input("Qual música você quer ouvir (nome do arquivo): ")
    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.play()
    
    while True:
        comando = input("Digitar (P) Pausar, (C) Continuar, (S) Sair: ")
        if comando == "P":
            pygame.mixer.music.pause()
        elif comando == "C":
            pygame.mixer.music.unpause()
        elif comando == "S":
            pygame.mixer.music.stop()
            break
        else:
            print("Comando inválido!")
    
except pygame.error:
    print("⚠️  Error: Arquivo não encontrado! Verifique o nome do arquivo. ")