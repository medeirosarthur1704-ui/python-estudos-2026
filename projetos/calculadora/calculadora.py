# ================================================================
# CALCULADORA
# Calculadora de terminal com 7 operações matemáticas (+, -, *, /,
# **, //, %), selecionadas via match/case. Trata erros de entrada
# inválida, divisão por zero e interrupção do usuário (Ctrl+C).
# ================================================================

from time import sleep      # cria uma pausa (efeito de "processando")
import pyfiglet             # gera o banner em ASCII art


try:

    # Banner de título, em vermelho
    banner = pyfiglet.figlet_format("Calculadora", font="slant")
    print(f"\033[1;38;2;255;0;0m{banner}\n")

    # Pede os dois números (já convertidos pra float, aceitam decimais)
    n1 = float(input("\033[1;38;2;255;140;0m \n[+] Digite o primeiro número: "))
    n2 = float(input("\033[1;38;2;255;140;0m \n[+] Digite o segundo número: "))

    # Pergunta qual operação o usuário quer fazer
    operação = input("\033[1;38;2;255;140;0m \n[+] Digite a operação (+, -, *, /, **, //, %): ")

    print("\033[1;38;2;180;0;255m[+] Calculando...")
    sleep(2)  # pausa só pra dar a sensação de "processamento"

    # match/case funciona como um "switch": compara 'operação' com
    # cada caso abaixo e executa o bloco correspondente
    match operação:

        case "+":
            resultado = f"\033[1;38;2;0;255;0m{n1 + n2:.0f}"

        case "-":
            resultado = f"\033[1;38;2;0;255;0m{n1 - n2:.0f}"

        case "*":
            resultado = f"\033[1;38;2;0;255;0m{n1 * n2:.0f}"

        case "/":
            # :.2f mantém 2 casas decimais (divisão raramente é número inteiro)
            resultado = f"\033[1;38;2;0;255;0m{n1 / n2:.2f}"

        case "**":
            resultado = f"\033[1;38;2;0;255;0m{n1 ** n2:.2f}"

        case "//":
            resultado = f"\033[1;38;2;0;255;0m{n1 // n2:.0f}"

        case "%":
            resultado = f"\033[1;38;2;0;255;0m{n1 % n2:.2f}"

        case _:
            # "_" é o caso padrão, cai aqui se não bater com nenhuma operação acima
            resultado = "\033[1;38;2;255;0;0m\n[-] Operação inválida"

    print(f"\033[1;38;2;0;255;255m\n[+] O resultado da operação é: {resultado}\033[0m")


# Cada except trata um tipo específico de erro que pode quebrar o programa:

except ValueError:
    print("\033[1;38;2;255;0;0m[-] Erro: Digite apenas números!")

except ZeroDivisionError:
    print("\033[1;38;2;255;0;0m[-] Erro: Não é possível dividir por zero.")

except KeyboardInterrupt:
    print("\033[1;38;2;255;20;147m[-] Operação cancelada pelo usuário.")