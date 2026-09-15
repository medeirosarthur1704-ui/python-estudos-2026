# ================================================================
# GERADOR DE SENHAS
# Gera uma senha aleatória e criptograficamente segura usando o
# módulo 'secrets', ideal pra criação de senhas fortes.
# ================================================================

from time import sleep       # pausa pra simular processamento
import secrets               # gera valores aleatórios seguros
import pyfiglet              # gera o banner em ASCII art

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("Gerador de Senhas", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")  # \033[1;38;2;255;0;0m é um código ANSI que muda a cor do texto para vermelho

print("\033[1;38;2;255;140;0m \n[+] Gerando uma senha aleatória segura...")
sleep(2)  # espera 2 segundos, só efeito visual

# token_hex(8) gera 8 bytes aleatórios e retorna como texto hexadecimal
# (cada byte vira 2 caracteres, então a senha final tem 16 caracteres)
# 'secrets' é preferível ao módulo 'random' aqui porque é criptograficamente seguro
senha = secrets.token_hex(8)

print(f"\033[1;38;2;0;150;255m\n[+] Sua senha é: \033[1;38;2;0;255;0m{senha}")