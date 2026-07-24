import qrcode

dados = input("Digite um link: ")
print("Analisando informações...")

imagem = qrcode.make(dados)

imagem.save("qr.png")

imagem.show()

print("QR Code gerado com sucesso!")