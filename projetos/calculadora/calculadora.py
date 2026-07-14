n1 = int(input("Digite o Primeiro Número: "))
n2 = int(input("Digite o Segundo Número: "))
operação = input("Digite a Operação: ")

match operação:
    case "+":
        resultado = f"{n1 + n2}✅"
    case "-":
        resultado =  f"{n1 - n2}✅"
    case "*":
        resultado = f"{n1 * n2}✅"
    case "/":
        resultado = f"{n1 / n2}✅"
    case "**":
        resultado = f"{n1 ** n2}✅"
    case "//":
        resultado = f"{n1 // n2}✅"
    case "%":
        resultado = f"{n1 % n2}✅"
    case _:
        resultado = "Operação Inválida❌"
        
print(f"O Resultado da Operação é: {resultado}")