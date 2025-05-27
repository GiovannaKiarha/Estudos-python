# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, intenger, float, boolean...

aluno = {'nome': 'Giovanna', 'idade': 27, 'nota_final': 'A', 'aprovação': True} # o primeiro é a key e o segundo é o value

aluno.update({'nome': 'Pedro', 'nota_final': 'B'}) # atualizando itens no dicionário. Sempre especifica key e depois value
print(aluno)

print(aluno.get('endereco', 'Não existe')) # nao retorna erro. Só retorna que o valor não existe. Consegue adicionr uma mensagem

del aluno['idade'] # remover
print(aluno)

# Looping dentro de um dicionário

for x in aluno.values(): # tem que especificar se vai ser key ou value. Items vai puxar as keys e os values, mas puxa como tupple
    print(x)

for keys, values in aluno.items(): # não puxa como tupple. Tira os valores de dentro da Tupple
    print(keys, values)

# Visualizando itens, keys e Values

