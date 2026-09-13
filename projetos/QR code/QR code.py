from time import sleep   # pausa pra simular processamento

import qrcode             # biblioteca externa que gera QR Codes

# Pede ao usuário o texto ou link que vai virar QR Code
dados = input("\033[1;34mDigite um link: ")

print("\033[1;35mGerando QR Code...")
sleep(2)  # só efeito visual, não afeta a geração do código

# qrcode.make() transforma o texto em uma imagem de QR Code (objeto de imagem)
imagem = qrcode.make(dados)

# Salva a imagem gerada como um arquivo PNG no diretório atual
imagem.save("qr.png")

# Abre a imagem automaticamente no visualizador padrão do sistema
imagem.show()

print("\033[1;32mQR Code gerado com sucesso!")