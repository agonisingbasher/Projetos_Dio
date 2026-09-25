import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

print("--- Gerador de Senhas Seguras ---")
tamanho_senha = int(input("Digite o tamanho da senha desejada (ex: 12): "))
print(f"Sua nova senha: {gerar_senha(tamanho_senha)}")
