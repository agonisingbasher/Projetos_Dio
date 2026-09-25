# Matemática simples: solicitar dois números e realizar uma operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == '+':
    print(f"Resultado da soma: {num1 + num2}")
elif operacao == '-':
    print(f"Resultado da subtração: {num1 - num2}")
elif operacao == '*':
    print(f"Resultado da multiplicação: {num1 * num2}")
elif operacao == '/':
    if num2 != 0:
        print(f"Resultado da divisão: {num1 / num2}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida.")
