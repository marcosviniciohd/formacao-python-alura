def solicite_um_numero():
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        print('Número par')
    else:
        print('Numero impar')

def faixa_etaria():
    idade = int(input('Digite sua idade: '))
    if 0 <= idade <= 12:
        print('Criança')
    elif 13 <= idade <= 18:
        print('Adolecente')
    else:
        print('Adulto')


if __name__ == '__main__':
    #solicite_um_numero()
    faixa_etaria()
