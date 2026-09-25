# Vamos solicitar uma string e um número inteiro como entrada
# Depois teremos que retornar a string repetida o número de vezes informado
texto = input("Digite uma palavra ou texto: ")
numero = int(input("Digite um número inteiro: "))

# Em Python, multiplicar uma string por um número inteiro repete a string
resultado = (texto + " ") * numero

print("Resultado:", resultado)
