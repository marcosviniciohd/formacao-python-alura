print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
chute = input("Digite o seu número da sorte: ")
chute = int(chute)
while(chute != 42):
    print("Você digitou ", chute)
    acerto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    if(acerto):
        print("Você acertou o número da sorte é" ,numero_secreto)
    else:
       if(maior):
           print("Você errou! O seu chute foi maior que o número secreto.")
       elif(menor):
           print("Você errou! O seu chute foi menor do que o número secreto.")