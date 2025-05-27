carros = ['BMW X6', 'BMW i5', 'BMW i8']

carro = str(input('Digite o carro que você quer comprar: '))

if carro.lower() in carros:
    print('Este carro está disponível')
else:
    print('Desculpe. Este carro não está disponível')