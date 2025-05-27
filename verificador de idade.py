idade = int(input('Digite a sua idade: '))

if idade < 13:
    print('Você é uma criança')
elif idade >=13 and idade <=19:
    print('Você é uma adolescente')
else:
    print('Você é um adulto')