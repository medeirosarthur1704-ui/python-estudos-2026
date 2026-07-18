from math import radians, sin, cos, tan

angulo_graus = float(input("Digite o ângulo que você deseja: "))
angulo_radianos = radians(angulo_graus)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f"O ângulo de {angulo_graus} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo_graus} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo_graus} tem a TANGENTE de {tangente:.2f}")