print("Python na escola de programção da Alura")
print('Python na Escola de Programação da Alura')

#Criação das variáveis
nome = 'Marcos Vinício'
idade = 39

#Abordagem simples
print('Meu nome é' ,nome, 'e tenho' ,idade, 'anos de idade')

print(f"Meu nome é {nome} e tenho {idade} anos.")

# Imprimir cada letra em uma linha
frase = "Python"
for letra in frase:
    print(letra)

print("==========================================")

escola = "ALURA"
for letra in escola:
    print(letra)


pi_arredondado = 3.14159
print(round(pi_arredondado, 2))


departamento = input("Departamento: ")
responsavel = input("Responsavel: ")
print("O departamento de " + departamento + " é liderado por " + responsavel)
