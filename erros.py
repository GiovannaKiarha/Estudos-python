# Trabalhando com Try e Except com uma lista
    # Excelente para testes
    # Não realiza o stop do programa
    # Mensagens customizadas quando encontra o erro
from operator import index

from Start import resultado

try:
    letras = ['a', 'b','c']
    print(letras[3])
except IndexError:
    print('Index não existe')


# Trabalho com Try e Except em Input

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
    print(valor)
except ValueError:
    print('Favor digitar apenas números')
finally:
    print('Código ok')
# else: # Só aparece quando o Try está okay
    #print('Usuário digitou um valor válido')
    #resultado = valor *2
    #print(resultado)

# Adicionando Else e Finally

