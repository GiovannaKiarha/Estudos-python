cidade = {
    'Brasil' : 'Brasília',
    'Argentina' : 'Buenos Aires',
    'Peru' : 'Lima',
    'Chile' : 'Santiago',
    'Austrália' : 'Canberra'
}

pais_usuario = input('Digite um país: ')

if pais_usuario in cidade:
    print(f'A capital do país {pais_usuario} é {cidade[pais_usuario]}')
else:
    print('Desculpe. Não temos informação sobre esse país')