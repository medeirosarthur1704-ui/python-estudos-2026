import pwinput

senha = pwinput.pwinput("Digite sua senha: ", mask = "*")

senha_oculta = "*" * len(senha)

print(f"Senha oculta: {senha_oculta}")
print("✅ Senha recebida com sucesso!")