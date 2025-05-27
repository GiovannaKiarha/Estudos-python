import math

print(math.ceil(4.2))
print(math.floor(4.2))
print(math.pow(4, 2))
print(math.sqrt(16)) # Raiz quadrada

'''
Math python librady no google para estudar mais
'''

# os detalhes de uma string
'''
Uma string é um texto. Sequência de caracteres dentro de uma variável
'''

mensagem = 'Este curso é muito bom'
print(mensagem)

# indexaçao e fatiamento (slice)

print(mensagem[3]) #indexação
print(mensagem[0:4]) #fatiamento. Para em um antes

# métodos comuns em string

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.strip()) #remove espaço em branco no início
print(mensagem.replace('bom', 'excelente')) #precisa especificar sempre
print(mensagem.split()) #separa palavra por palavra

# utiliando f-string

nome = 'Giovanna'
idade = 27

print('O meu nome é', nome, 'e tenho', idade, 'anos de idade')

'''
Formatação de f-string. Sempre utilizar ela
'''

print(f'O meu nome é {nome} e tenho {idade} anos de idade')

# scape sequences ou sequências de escape

mensagem = 'coluna1\tcoluna2\tcoluna3' # tabulaçao
print(mensagem)

mensagem = 'Aprender python é \nmuito fácil' # quebra de linha
print(mensagem)

mensagem = 'c:\\Users\\Giovanna' # para mostrar barra invertida, adiciona duas barras invertidas
print(mensagem)

mensagem = 'Aprender \'python\' é muito divertido' # para mostrar aspas
print(mensagem)

# tabulações e unicode com strings

mensagem = 'Nome:\tGiovanna Kiarha\nIdade:\t27\nPaís:\tBrasil'
# caracteres unicode
mensagem2 = 'Coração: \u2764' # tem uma tabela com os códigos
print(mensagem)
print(mensagem2)
