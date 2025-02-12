from array import array

# Arrays
    # Usa quando vão ter muitos itens diferente de list
    # Melhor performance
    # Não está disponível no Python. Tem que importar

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u',['a', 'b', 'c', 'd'] ) # typecode digita no google e acha a documentação do python em array
numeros_i = array('i', [10, 20, 30, 40]) # não pode informar typecode errado. TOMAR CUIDADO
numeros_f = array('f',[1.2, 2.2, 3.2] )

print(letras)
print(numeros_i)
print(numeros_f)



