# ================================================================
# QR CODE GENERATOR
# Gera uma imagem de QR Code a partir de um link/texto digitado
# pelo usuário, salva como PNG e abre automaticamente na tela.
# ================================================================

from time import sleep       # pausa pra simular processamento
import pyfiglet              # gera o banner em ASCII art
import qrcode                # biblioteca externa que gera QR Codes

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("QR Code Generator", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")

# Pede ao usuário o texto ou link que vai virar QR Code
dados = input("\033[1;34m\n[+] Digite um link: ")

print("\033[1;35m\n[+] Gerando QR Code...")
sleep(2)  # só efeito visual, não afeta a geração do código

# qrcode.make() transforma o texto em uma imagem de QR Code (objeto de imagem)
imagem = qrcode.make(dados)

# Salva a imagem gerada como um arquivo PNG no diretório atual
imagem.save("qr.png")

# Abre a imagem automaticamente no visualizador padrão do sistema
imagem.show()

print("\033[1;32m\n[+] QR Code gerado com sucesso!")