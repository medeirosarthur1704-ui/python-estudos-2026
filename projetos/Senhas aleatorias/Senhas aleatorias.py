import secrets
from time import sleep

senha = secrets.token_hex(8)
print("GERANDO SENHA...")
sleep(2)
print(senha)