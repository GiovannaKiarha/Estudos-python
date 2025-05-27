altura = float(input('Qual a sua altura em cm: '))
peso = float(input('Qual o seu pego em kg: '))

def calculo_imc():
    imc = peso / (altura/100)**2
    if imc < 18.5:
        print('Magreza')
    elif range in (18.5,24.9):
        print('Normal')
    elif range in (25, 29.9):
        print('Sobrepeso')
    elif range in (30, 39.9):
        print('Obesidade')
    elif imc >= 40:
        print('Obesidade grave')

calculo_imc()