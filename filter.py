from sys import getsizeof

 # filter function
    # muito utilizado em listas
    # aplicar uma função a um Iterable, filtrando os items.

valores = [10, 12, 34, 44, 57]

# def remover20(x):
    # return x > 20

# print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))

# Entendendo List Comprehension com Strings

 #forma mais simples de se escrever
 #utilizado quando precisa criar uma nova lista a partir de uma existente

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

#frutas2 = []

#for itens in frutas1:
#   if 'b' in itens:
#      frutas2.append(itens)

frutas2 = [iten for iten in frutas1 if 'n' in iten]

print(frutas2)

# entendendo list comprehension com números
    # mais simples de se escrever
    # utilizando quando você precisa criar uma nova lista a partir de uma existente
    # expressão for itens in itens

#valores = []

#for x in range(6):
#    valores.append(x * 10)

#print(valores)

valores = [x * 10 for x in range(6)]
print(valores)

# Lista e Generator Expressions
    # Uma forma mais rápida para listas, dicionário e etc
    # Menos memória alocada
    # Valores em Bytes

numeros = [x * 10 for x in range(5)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('======')

numeros = (x * 10 for x in range(5))
print(list(numeros))
print(type(numeros))
print(getsizeof(numeros)) # gasta menos memória
