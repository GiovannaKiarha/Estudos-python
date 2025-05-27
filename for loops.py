print('Loop com o break:')
for numero in range (1, 11):
    if numero > 5:
        break
    print(numero)

print('Loop com o continue:')
for numero in range (1,11):
    if numero == 5: # nao imprimi o numero 5
        continue
    print(numero)

