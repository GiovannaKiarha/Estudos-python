cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador') #imutável. Não é lista. Lista é mutável

cidade_usuario = str(input('Digite o nome de uma cidade: '))

if cidade_usuario in cidades:
    print('Parabéns. Você acertou a cidade')
else:
    print('Errou. Tente novamente')