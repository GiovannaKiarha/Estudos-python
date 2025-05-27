
frutas = ['maçã', 'banana', 'manga', 'uva']
print(frutas[0])
print(frutas[3])

frutas[1] = 'morango'
frutas.append('abacaxi') # adicionar item na lista
print(frutas)

frutas.remove('manga')
del frutas[-1] # remove o último item
print(frutas)

