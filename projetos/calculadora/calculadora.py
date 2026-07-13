num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operação = input("Digite a operação: ")

match operação:
    case "+":
        resultado = f"{num1 + num2}✅"
    case "-":
        resultado = f"{num1 - num2}✅"
    case "*":
        resultado = f"{num1 * num2}✅"
    case "/":
        resultado = f"{num1 / num2}✅"
    case "**":
        resultado = f"{num1 ** num2}✅"
    case "//":
        resultado = f"{num1 // num2}✅"
    case "%":
        resultado = f"{num1 % num2}✅"
    case _:
        resultado = "Operação inválida❌"
        
print(f"O resultado da operação é: {resultado}")