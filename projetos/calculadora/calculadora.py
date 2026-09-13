from time import sleep      # importa sleep, usado pra criar uma pausa (efeito de "processando")
import pyfiglet             # importa a lib que gera o banner em ASCII art

try:
    # Imprime o título "Calculadora" estilizado com a fonte "slant"
    print(pyfiglet.figlet_format("Calculadora", font="slant"))

    # Pede o primeiro número; já converte pra float (aceita decimais)
    n1 = float(input("\033[1;33mDigite o primeiro número: "))
    # Pede o segundo número, também como float
    n2 = float(input("\033[1;33mDigite o segundo número: "))
    # Pergunta qual operação o usuário quer fazer (texto, sem conversão)
    operação = input("\033[1;33mDigite a operação (+, -, *, /, **, //, %): ")

    print("\033[1;35mCalculando...")
    sleep(1)  # Pausa de 1 segundo só pra dar a sensação de "processamento"

    # match/case funciona como um "switch": compara o valor de 'operação'
    # com cada caso abaixo e executa o bloco correspondente
    match operação:
        case "+":
            # :.0f formata o resultado sem casas decimais
            resultado = f"\033[1;32m{n1 + n2:.0f}"
        case "-":
            resultado = f"\033[1;32m{n1 - n2:.0f}"
        case "*":
            resultado = f"\033[1;32m{n1 * n2:.0f}"
        case "/":
            # :.2f mantém 2 casas decimais (divisão raramente é número inteiro)
            resultado = f"\033[1;32m{n1 / n2:.2f}"
        case "**":
            # potenciação (n1 elevado a n2)
            resultado = f"\033[1;32m{n1 ** n2:.2f}"
        case "//":
            # divisão inteira (arredonda pra baixo, descarta o resto)
            resultado = f"\033[1;32m{n1 // n2:.0f}"
        case "%":
            # módulo/resto da divisão
            resultado = f"\033[1;32m{n1 % n2:.2f}"
        case _:
            # "_" é o caso padrão, cai aqui se não bater com nenhuma operação acima
            resultado = "\033[1;31mOperação inválida"

    print(f"\033[1;32mO resultado da operação é: {resultado}")

# Cada except trata um tipo específico de erro que pode quebrar o programa:
except ValueError:
    # Acontece se o usuário digitar algo que não é número no input
    print("\033[1;31mErro: Digite apenas números!")
except ZeroDivisionError:
    # Acontece se tentar dividir por zero (/ , // ou %)
    print("\033[1;31mErro: Não é possível dividir por zero.")
except KeyboardInterrupt:
    # Acontece se o usuário apertar Ctrl+C no meio da execução
    print("\033[1;34mOperação cancelada pelo usuário.")