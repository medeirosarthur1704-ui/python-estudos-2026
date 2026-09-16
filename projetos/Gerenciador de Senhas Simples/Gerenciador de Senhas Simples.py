# ================================================================
# SENHA SEGURA
# Sistema de criação e confirmação de senha protegido por PIN: a
# senha é digitada de forma mascarada e só é revelada na tela se
# o usuário informar corretamente o PIN de 4 dígitos criado no
# início do programa.
# ================================================================

from time import sleep
import pyfiglet
import pwinput          # permite digitar senha no terminal mostrando "*" no lugar dos caracteres

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("Senha Segura", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")


# --- Etapa 1: criar um PIN de 4 dígitos ---

pin = input("\033[1;36m\n[+] Crie um PIN de 4 dígitos: ")

# Repete a pergunta enquanto o PIN não tiver exatamente 4 caracteres
# ou enquanto ele não for composto só por dígitos (isdigit())
while len(pin) != 4 or not pin.isdigit():
    print("\033[1;31mO PIN precisa ter exatamente 4 números.")
    pin = input("\033[1;36m\n[+] Crie um PIN de 4 dígitos: ")


# --- Etapa 2: criar e confirmar a senha ---

try:

    while True:

        # pwinput funciona como input(), mas exibe "*" em vez do texto digitado
        senha = pwinput.pwinput("\033[1;33m\n[+] Digite a senha: ", mask="*")
        confirmar = pwinput.pwinput("\033[1;33m\n[+] Confirme a senha: ", mask="*")

        print("\033[1;35m\n[+] Verificando a senha...")
        sleep(2)

        if senha == confirmar:
            print("\033[1;32mSenha confirmada com sucesso!")

            # Pergunta se o usuário quer revelar a senha na tela
            ver = input("\033[1;33m\n[+] Deseja ver a senha? [S/N] ").strip().upper()

            if ver == "S":
                # Só mostra a senha se o PIN criado no início bater
                pin_digitado = input("\033[1;33m\n[+] Digite seu PIN para ver a senha: ")

                if pin_digitado == pin:
                    print(f"\033[1;32mSua senha é: {senha}")
                else:
                    print("\033[1;31m[-] PIN incorreto. A senha continuará oculta.")
            else:
                print("\033[1;33m[-] Senha mantida oculta.")

            break  # sai do laço while True, processo concluído

        else:
            print("\033[1;31m[-] As senhas não coincidem. Tente novamente.")

except KeyboardInterrupt:
    print("\n\033[1;31m[-] Processo interrompido pelo usuário.")