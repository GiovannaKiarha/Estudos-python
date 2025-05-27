# Lambda function
    # É uma função (pequena) sem nome
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentre de outras funções
    # Código mais 'clean'

def somar(x):
    return x + 10

print(somar(2))

somar10 = lambda x: x+ 10 # primeiro argumento que é o x e a expressão é depois dos dois pontos
print(somar10(2))

# Lambda dentro de função

def somar(x):
    func2 = lambda x: x + 10 # tem que sempre associar a variável
    return func2(x) * 4

print(somar(2))