from time import sleep       # pausa pra simular processamento
import secrets               # módulo padrão do Python pra gerar valores aleatórios seguros

print("\033[1;36mGerando uma senha aleatória segura...")
sleep(2)  # espera 2 segundos, só efeito visual

# token_hex(8) gera 8 bytes aleatórios e retorna como texto hexadecimal
# (cada byte vira 2 caracteres, então a senha final tem 16 caracteres)
# 'secrets' é preferível ao módulo 'random' aqui porque é criptograficamente seguro
senha = secrets.token_hex(8)

print(f"\033[1;32mSua senha é: \033[1;33m{senha}")