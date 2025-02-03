# For loops
from operator import truediv

# imprimir de 1 a 5

for numero in range(6):
    print(numero)

# for loops utilizando strings

for letra in 'Google':
    print(letra)

palavra = 'Google'

for letra in palavra:
    print(palavra)

for letra in palavra:
    print(f' {letra} está dentro da palavra {palavra}')

# for loops utilizando if e else
# enviar um email com os detalhes da compra online (maximo 3 tentativas) para comprar confirmadas

compra_confirmada = True
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu email')
        break
else:
    print('Falha na compra')

# for loop: nested loops

for numero1 in range (5): #loop de fora - outer loop
    print(numero1)
    for numero2 in range(5): #loop de dentro - inner loop
        print(numero2)

# for loop : separando strings

# modificar a palavra FANTASTICO para F A N T A S T I C O

palavra = 'FANTASTICO'

for espaco in palavra:
    print(f' {espaco}', end = '')

# for loop criando um retangulo

linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()

'''
Conhecendo o while loops
'''
# excelente para loops dependentes de uma condição

# criar uma promoção para um produto no valor de R$100

valor = 100
dia = 1

while valor > 20:
    dia +=1
    print(f' No dia {dia} o produto vai ser vendido por {valor}')
    print(valor)
    valor -=5

'''
operador ternário
'''

idade = 14

resultado = 'Voto permitido' if idade >=16 else 'Voto não permitido'

print(resultado)

'''
criando condições com while loop
'''

valor = int(input('Digite o valor do seu produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será R${valor}')
    break # não é a melhor forma de parar o looping do while 