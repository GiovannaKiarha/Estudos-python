# Operadores de comparação

a = 10
b = 20

print(a==b) # dá uma resposta boolean. Se é true ou false. == se é igual
print(a!=b) # != é para diferença
print(a>b) # > maior ou menor do que algo
print(a<b)
print(a>=b) # maior ou igual ou menor ou igual

# utilizando o if

idade = int(input('Digite a sua idade:'))

if idade>=18:
    print('Maior de idade')
else:
    print('Menor de idade')

# utilizando o elif. Usa quando não é nem uma e nem a outra. Pode ser visto como OU. Pode adicionar quantos quiser desde que coloque a condição

idade = int(input('Digite a sua idade:'))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade < 60: # dá para simplificar
    print('Maior de idade')
else:
    print('Idoso')
