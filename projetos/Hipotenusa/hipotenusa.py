# ================================================================
# HIPOTENUSA
# Calcula a hipotenusa de um triângulo retângulo a partir dos
# catetos oposto e adjacente, usando o módulo padrão 'math'.
# ================================================================

from math import hypot     # calcula a hipotenusa direto: hypot(a, b) = sqrt(a² + b²)
import pyfiglet            # gera o banner em ASCII art

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("Hipotenusa", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")

# Pede os dois catetos do triângulo
co = float(input("\033[1;38;2;255;140;0m \n[+] Digite o cateto oposto: "))
ca = float(input("\033[1;38;2;255;140;0m \n[+] Digite o cateto adjacente: "))

# hypot() já aplica o Teorema de Pitágoras (a² + b² = c²) e tira a raiz quadrada
hi = hypot(co, ca)

print(f"\033[1;38;2;0;255;0m\n[+] A hipotenusa vai medir: {hi:.2f}")