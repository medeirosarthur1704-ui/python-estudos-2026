import pygame
import time

pygame.mixer.init()

try:
    nome_arquivo = input("Qual música você quer tocar? (nome do arquivo): ")
    pygame.mixer.music.load(nome_arquivo)
    pygame.mixer.music.play()

    while True:
        comando = input("Digite (p) pausar, (c) continuar, (s) sair: ")
        if comando == "p":
            pygame.mixer.music.pause()
        elif comando == "c":
            pygame.mixer.music.unpause()
        elif comando == "s":
            pygame.mixer.music.stop()
            break
        else:
            print("Comando inválido!")

except pygame.error:
    print("⚠️  Erro: Arquivo não encontrado! Verifique o nome digitado.")