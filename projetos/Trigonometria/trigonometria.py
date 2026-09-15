from math import radians, sin, cos, tan
from time import sleep
import pyfiglet

banner = pyfiglet.figlet_format("Trigonometria", font = "slant")
print(f"\033[1;38;2;255;40;40m{banner}\n")

angulo_graus = float(input("\033[1;34m\n[+] Digite o ângulo que você deseja: "))
angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f"\033[1;95m\n[+] O ângulo de {angulo_graus} tem o SENO de \033[1;32m{seno:.2f}")
print(f"\033[1;95m\n[+] O ângulo de {angulo_graus} tem o COSSENO de \033[1;32m{cosseno:.2f}")
print(f"\033[1;95m\n[+] O ângulo de {angulo_graus} tem a TANGENTE de \033[1;32m{tangente:.2f}")