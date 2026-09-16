# ================================================================
# TRIGONOMETRIA
# Calcula seno, cosseno e tangente de um ângulo (em graus)
# informado pelo usuário, usando o módulo padrão 'math'.
# ================================================================

from math import radians, sin, cos, tan   # funções trigonométricas do Python
import pyfiglet                            # gera o banner em ASCII art

# Banner de título, em vermelho vivo
banner = pyfiglet.figlet_format("Trigonometria", font="slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")

# Pede o ângulo em graus
angulo_graus = float(input("\033[1;38;2;255;140;0m \n[+] Digite o ângulo que você deseja: "))

# As funções sin/cos/tan do Python trabalham em radianos, não em graus,
# por isso é preciso converter antes de calcular
angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f"\033[1;38;2;0;255;0m\n[+] O ângulo de {angulo_graus} tem o SENO de {seno:.2f}")
print(f"\033[1;38;2;0;255;255m[+] O ângulo de {angulo_graus} tem o COSSENO de {cosseno:.2f}")
print(f"\033[1;38;2;255;0;255m[+] O ângulo de {angulo_graus} tem a TANGENTE de {tangente:.2f}")