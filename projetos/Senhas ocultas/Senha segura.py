from time import sleep
import pyfiglet
import pwinput

print(pyfiglet.figlet_format("Bem-vindo!", font="slant"))

# Criar PIN
pin = input("\033[1;36mCrie um PIN de 4 dígitos: ")

while len(pin) != 4 or not pin.isdigit():
    print("\033[1;31mO PIN precisa ter exatamente 4 números.")
    pin = input("\033[1;36mCrie um PIN de 4 dígitos: ")

# Confirmar a senha
try:
    while True:
        senha = pwinput.pwinput("\033[1;33mDigite a senha: ", mask="*")
        confirmar = pwinput.pwinput("\033[1;33mConfirme a senha: ", mask="*")

        print("\033[1;35mVerificando a senha...")
        sleep(2)

        if senha == confirmar:
            print("\033[1;32mSenha confirmada com sucesso!")

            ver = input("Deseja ver a senha? [S/N] ").strip().upper()

            if ver == "S":
                pin_digitado = input("Digite seu PIN para ver a senha: ")

                if pin_digitado == pin:
                    print(f"\033[1;32mSua senha é: {senha}")
                else:
                    print("\033[1;31mPIN incorreto. A senha continuará oculta.")

            else:
                print("\033[1;33mSenha mantida oculta.")

            break

        else:
            print("\033[1;31mAs senhas não coincidem. Tente novamente.")

except KeyboardInterrupt:
    print("\n\033[1;31mProcesso interrompido pelo usuário.")