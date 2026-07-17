try:
    n1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))
    n2 = int(input("DIGITE O SEGUNDO NÚMERO: "))
    operação = input("DIGITE A OPERAÇÃO: ")

    match operação:
        case "+":
            resultado = n1 + n2
        case "-":
            resultado = n1 - n2
        case "*":
            resultado = n1 * n2
        case "/":
            resultado = n1 / n2
        case "**":
            resultado = n1 ** n2
        case "//":
            resultado = n1 // n2
        case "%":
            resultado = n1 % n2
        case _:
            resultado = "OPERAÇÃO INVÁLIDA"

    print(f"O RESULTADO DA OPERAÇÃO É: {resultado}")

except ValueError:
    print("DIGITE APENAS NÚMEROS.")
except ZeroDivisionError:
    print("NÃO É POSSÍVEL DIVIDIR POR ZERO.")