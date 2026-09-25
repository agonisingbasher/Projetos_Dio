
print("--- 🎮 Jogo da Adivinhação ---")
print("Escolha o nível de dificuldade:")
print("1 - Fácil   (1 a 10  | 5 tentativas)")
print("2 - Médio   (1 a 50  | 4 tentativas)")
print("3 - Difícil (1 a 100 | 3 tentativas)")

escolha = input("Digite a opção desejada (1, 2 ou 3): ")

if escolha == '1':
    limite = 10
    tentativas = 5
elif escolha == '2':
    limite = 50
    tentativas = 4
elif escolha == '3':
    limite = 100
    tentativas = 3
else:
    print("Opção inválida. Nível Fácil selecionado por padrão.")
    limite = 10
    tentativas = 5

numero_secreto = random.randint(1, limite)
print(f"\nJogo iniciado! Tente adivinhar o número entre 1 e {limite}.")

while tentativas > 0:
    chute = int(input(f"Seu palpite (Tentativas restantes: {tentativas}): "))
    
    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou o número secreto!")
        break
    elif chute < numero_secreto:
        print("📉 Errou! O número secreto é MAIOR.")
        tentativas -= 1
    else:
        print("📈 Errou! O número secreto é MENOR.")
        tentativas -= 1

if tentativas == 0:
    print(f"💀 Fim de jogo! Você esgotou suas tentativas. O número era {numero_secreto}.")