from time import sleep
import pyfiglet
import pwinput          # lib externa que permite digitar senha no terminal mostrando "*" no lugar dos caracteres

# Banner de boas-vindas em ASCII art
print(pyfiglet.figlet_format("Bem-vindo!", font="slant"))

# --- Etapa 1: criar um PIN de 4 dígitos ---
pin = input("\033[1;36mCrie um PIN de 4 dígitos: ")

# Repete a pergunta enquanto o PIN não tiver exatamente 4 caracteres
# ou enquanto ele não for composto só por dígitos (isdigit())
while len(pin) != 4 or not pin.isdigit():
    print("\033[1;31mO PIN precisa ter exatamente 4 números.")
    pin = input("\033[1;36mCrie um PIN de 4 dígitos: ")

# --- Etapa 2: criar e confirmar a senha ---
try:
    while True:
        # pwinput funciona como input(), mas exibe "*" em vez do texto digitado
        senha = pwinput.pwinput("\033[1;33mDigite a senha: ", mask="*")
        confirmar = pwinput.pwinput("\033[1;33mConfirme a senha: ", mask="*")

        print("\033[1;35mVerificando a senha...")
        sleep(2)

        if senha == confirmar:
            print("\033[1;32mSenha confirmada com sucesso!")

            # Pergunta se o usuário quer revelar a senha na tela
            ver = input("Deseja ver a senha? [S/N] ").strip().upper()

            if ver == "S":
                # Só mostra a senha se o PIN criado no início bater
                pin_digitado = input("Digite seu PIN para ver a senha: ")

                if pin_digitado == pin:
                    print(f"\033[1;32mSua senha é: {senha}")
                else:
                    print("\033[1;31mPIN incorreto. A senha continuará oculta.")
            else:
                print("\033[1;33mSenha mantida oculta.")

            break  # sai do laço while True, processo concluído

        else:
            # Se as senhas não baterem, o laço volta pro topo e pergunta de novo
            print("\033[1;31mAs senhas não coincidem. Tente novamente.")

except KeyboardInterrupt:
    # Se o usuário apertar Ctrl+C a qualquer momento dentro do try
    print("\n\033[1;31mProcesso interrompido pelo usuário.")