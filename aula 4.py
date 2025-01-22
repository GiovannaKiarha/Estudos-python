# função input

nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')
pais_mora = input('Digite o país onde mora:')

print(f'Olá, {nome}! Seja bem vindo(a). Você tem {idade} e mora no {pais_mora}')

# convertendo de string para integer

nome = input('Digite o seu nome:')
idade = int(input('Digite a sua idade:')) # para converter para integer

print(type(nome))
print(type(idade))

# criando um programa com input

valor_produto = float(input('Digite o valor do seu produto:')) # captura do valor do produto

# calcula o valor com 10% de acréscimo

valor_final = valor_produto * 1.10

# Exibir o valor final na tela

print(f'O valor final do produto com acréscimo de 10% é: R$ {valor_final:.2f}')

# múltiplas entradas na mesma linha de input

dados = input('Digite o seu nome e idade: ').split()
nome = dados[0]
idade = dados [1]

print(f'Meu nome é {nome} e tenho {idade} anos de idade')

# criando uma entrada formatada

print(f'Meu nome é {nome.upper()} e tenho {idade} anos de idade') # para modificar a forma da letra, coloca a função dentro da variável que vai ser chamada

