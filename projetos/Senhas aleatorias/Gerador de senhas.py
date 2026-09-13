from time import sleep
import secrets

print("\033[1;36mGerando uma senha aleatória segura...")
sleep(2)
senha = secrets.token_hex(8)
print(f"\033[1;32mSua senha é: {senha}")