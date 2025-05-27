# looping dentro de uma lista

# armazenar mais de uma informação em variáveis
# manter a sequencias dos dados de uma variável

valores = [50, 80, 110, 150, 170]

for x in valores:
    print(f' O valor final do produto é de R$ {x}.')

# Isso acaba diminuindo linhas e facilitando o código

# verificando itens em uma lista

cor_cliente = input('Digite a cor desejada:')
cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']

if cor_cliente.lower() in cores: # isso é bom para caso o usuário coloque em letra minuscula ou maiuscula
    print('Em estoque')
else:
    print('Não temos essa cor em estoque')

# agregando duas listas com zip

cores = ['Amarelo', 'Verde', 'Azul', 'Vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))

var = list('comprar') # função que já existe no python. Divide cada caracter sendo um index
print(var)

# input em uma lista

# criar uma lista de frutas a partir do input fornecido pelo usuário

frutas_usuario = input('Digite o nome das frutas separados por vírgula: ')

frutas_lista = frutas_usuario.split(', ') # separa a lista toda vez que visualizar uma vírgula. Entre parenteses tu coloca a condição

print(frutas_lista)





