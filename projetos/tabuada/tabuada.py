import pyfiglet

banner = pyfiglet.figlet_format("Tabuada")
print(f"\033[1;38;2;255;40;40m{banner}\n")  # \033[1;38;2;255;0;0m é um código ANSI que muda a cor do texto para vermelho

num = int(input("\033[1;34m\n[+] Digite um número: "))
for i in range(1, 11):
    print(f"\033[1;35m{num} x {i} = {num * i}")