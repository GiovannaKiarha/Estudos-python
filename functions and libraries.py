# functions
from Start import resultado


# função foi feita para não ficar se repetindo

# quando vai criar uma função, usa o def

def boas_vindas():
    print('Olá, Giovanna')
    print('Temos 5 laptops no estoque')

boas_vindas()

# criando uma função de soma

def somar_dois_numeros():
    variavel1 = 10
    varial2 = 5
    resultado = variavel1 + varial2
    print(resultado)

# as variáveis podem ter o mesmo nome se estiver em funções diferentes. O python trabalha com blocos

# parâmetros e argumentos em uma função

def boas_vindas_teste(nome,quantidade): # parametro não default
    print(f'Olá, {nome}')
    print(f'Temos {str(quantidade)} laptops')

boas_vindas_teste('Giovanna', 5) #argumento
boas_vindas_teste('Leia', 4)
boas_vindas_teste('Yume', 3)

'''
def boas_vindas_Giovanna():
    print('Olá, Giovanna')
    print('Temos 5 laptops no estoque')

def boas_vindas_Leia():
    print('Olá, Leia')
    print('Temos 4 laptops no estoque')

def boas_vindas_Yume():
    print('Olá, Yume')
    print('Temos 3 laptops no estoque')
'''

# argumentos default(define o valor no parametro) and non default(não define o valor no parametro)

def boas_vindas_teste(nome,quantidade = 6): # parametro default tem que estar SEMPRE no final
    print(f'Olá, {nome}')
    print(f'Temos {str(quantidade)} laptops')

# print ou return em funçoes

def cliente1(nome):
    print(f'Olá{nome}')

def cliente2(nome):
    return f'Olá, {nome}' # joga para a memória e depois pode jogar na tela

x = cliente1('Maria')
y = cliente2('Yume')

print(x)
print(y)

# vários argumentos xargs com números
# criar uma função que soma vários numeros

def soma(*numeros): # * identifica vários argumentos
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x =  soma(2,3,5,7)
print(x)

# vários argumentos xargs nomeando os parametros

def agencia(**carro): # ** identifica vários parametros
    return

print(agencia(marca = 'gol',cor = 'branca',motor = 1.0))

