# Realizando cálculos com números

num1 = 10
num2 = 5
resultado = num1 + num2

'''
Se tiver divisão quebrada, o / dará as partes inteiras e o % dará o resto
'''

print(num1)
print(num2)
print(resultado)

print(10+5)
print(10-5)
print(10*5)
print(10/5)

# Cálculo com variáveis

alunos_presentes = 23
alunos_ausentes = 17
total_alunos = alunos_ausentes + alunos_presentes

print(total_alunos)

'''
Não dá para somar variáveis de tipos diferentes
'''
pro1 = 10
pro1 += 3 # Operador de atribução aumentada
resultado = pro1

print(resultado)

# Funções básicas para números
num1 = 3.145

print(num1)
print(round(num1)) # Arredondar para o inteiro mais próximo
print(round(num1, 3)) # Coloca o número com o número de casas decimais especificado

print(pow(2, 3)) # Número elevado. Primeiro o número e depois da potencia que será elevado

print(max(1, 4, 9, 2, 17, 3)) # Número máximo dentro da sequência
print(min(1, 4, 9, 2, 17, 3)) # Número mínimo dentro da sequência
print(sum([1, 4, 9, 2, 17, 3])) # Soma dos números dentro da sequência

# A ordem dos operadores faz a diferença

resultado = 10 + 5 * 2 - 3
print(resultado)





