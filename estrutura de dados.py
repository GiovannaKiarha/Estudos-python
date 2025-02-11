# introdução a listas
from traceback import print_tb

cidades = ['Rio de janeiro', 'São Paulo', 'Salvador']
cidades.append('Brasília') # função dentro de lista
print(cidades)

jogos = ['Dead by Daylight', 'Marvel Rivals', 'Fortnite']
jogos.remove('Fortnite') #função
print(jogos)
print(jogos[1])

# manipulando listas

numeros = [1, 2, 3, 4]
numeros[0] = 5 # para manipular sem mexer na lista
numeros.insert(1, 3) #função
print(numeros[0]) # puxa o index que quer
print(numeros[-1])

# funções dentro da lista

# existe uma lista oficial do python sobre funções dentro de lista

# concatenando listas
final = numeros * 2
print(final)

teste = numeros + jogos # dá para fazer com função também
numeros.extend(jogos)
print(teste)

# lista dentro de lista
itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[1])
print(itens[0])
print(itens[1][1])

# extraindo variáveis de uma lista

produtos = ['laranja', 'toddy', 'leite']

item1 = produtos[1]
print(item1)

# coisas que são iguais unpacking lists

produtos = ['arroz', 'feijão', 'laranja', 'banana']

item1, item2, item3, item4 = produtos
item1, item2, item3, *outros = produtos # são todos os outros itens

print(item1)
print(item2)
print(item3)
print(item4)








