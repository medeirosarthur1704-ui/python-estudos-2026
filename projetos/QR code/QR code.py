from time import sleep

import qrcode

dados = input("Digite um link: ")
print("PROCESSANDO...")
sleep(3)

imagem = qrcode.make(dados)

imagem.save("qr.png")

imagem.show()

print("QR Code gerado com sucesso!")