from math import hypot # função que calcula a hipotenusa a partir dos catetos
import pyfiglet  # biblioteca pra gerar banners em ASCII art
from time import sleep # cria uma pausa (efeito de "processando")

banner = pyfiglet.figlet_format("Hipotenusa", font = "slant") 
print(f"\033[1;38;2;255;40;40m{banner}\n")  # \033[1;38;2;255;0;0m é um código ANSI que muda a cor do texto para vermelho

co = float(input("\033[1;34m\n[+] Digite o cateto oposto: ")) 
ca = float(input("\033[1;34m\n[+] Digite o cateto adjacente: "))
print("\033[1;35m\n[+] Calculando a hipotenusa...")
sleep(2)  # só efeito visual, não afeta o cálculo
hi = hypot(co, ca)
print(f"\033[1;95m\n[+] A hipotenusa vai medir: \033[1;32m{hi:.2f}")  