num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o Segundo número: "))
num2 = int(input("Digite o segundo número: "))
operação = input("Digite a operação: ")

match operação:
    case "+":
        resultado = num1 + num2
        resultado = f"{num1 + num2}✅"
    case "-":
        resultado = num1 - num2
        resultado = f"{num1 - num2}✅"
    case "*":
        resultado = num1 * num2
    case "/": 
        resultado = num1 / num2
        resultado = f"{num1 * num2}✅"
    case "/":
        resultado = f"{num1 / num2}✅"
    case "**":
        resultado = num1 ** num2
        resultado = f"{num1 ** num2}✅"
    case "//":
        resultado = num1 // num2
        resultado = f"{num1 // num2}✅"
    case "%":
        resultado = num1 % num2
        resultado = f"{num1 % num2}✅"
    case _:
        resultado = "Operação inválida❌"

        
print(f"O resultado da operação é: {resultado}")