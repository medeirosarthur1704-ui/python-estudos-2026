try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    operação = input("Digite a operação: ")
    match operação:
        case "+":
            resultado = f"{n1 + n2:.0f}✅"
        case "-":
            resultado = f"{n1 - n2:.0f}✅"
        case "*":
            resultado = f"{n1 * n2:.0f}✅"
        case "/":
            resultado = f"{n1 / n2:.2f}✅"
        case "**":
            resultado = f"{n1 ** n2:.2f}✅"
        case "//":
            resultado = f"{n1 // n2:.0f}✅"
        case "%":
            resultado = f"{n1 % n2:.2f}✅"
        case _:
            resultado = "❌ Operação inválida"
    
    print(f"O resultado da operação é: {resultado}")
except ValueError:
    print("⚠️  Erro: Digite apenas números!")
except ZeroDivisionError:
    print("⚠️  Erro: Não é possivel dividir por zero.")
    