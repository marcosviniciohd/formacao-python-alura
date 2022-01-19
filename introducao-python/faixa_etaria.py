idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if(idade > 18):
    print("Você é maior de idade.")

else:
    if(idade < 12):
        print("Você é maior de criança.")
    elif(idade > 12):
        print("Você é um adolescente")