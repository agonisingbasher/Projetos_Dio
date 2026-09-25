import random

print("--- Jogo da Adivinhação ---")
numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    chute = int(input(f"Adivinhe um número entre 1 e 10 (Tentativas restantes: {tentativas}): "))
    
    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    else:
        print("❌ Errou!")
        tentativas -= 1

if tentativas == 0:
    print(f"Fim de jogo! O número secreto era {numero_secreto}.")
