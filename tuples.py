# entendendo sobre tuples
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
    # Não podem ser alteradas (Immutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
print(duas_listas)

duas_listas_tuple = cores_tuple * 2
print(duas_listas_tuple)

cores_list.append('Roxo') # não consegue adicionar itens em tuple que nem nas listas
print(cores_list)

# lista gasta um tamanho maior de memória do que tuple. Usa lista quando precisa mudar e tuple quando não vai mudar