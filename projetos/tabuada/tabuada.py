# ================================================================
# TABUADA
# Gera a tabuada (de 1 a 10) de um número escolhido pelo usuário.
# ================================================================

import pyfiglet          # gera o banner em ASCII art

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("Tabuada", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")

# Pede o número que o usuário quer ver a tabuada
num = int(input("\033[1;34m\n[+] Digite um número: "))

# Percorre de 1 até 10 (range(1, 11) exclui o 11) multiplicando 'num' por cada 'i'
for i in range(1, 11):
    print(f"\033[1;35m{num} x {i} = \033[1;33m{num * i}\033[0m")