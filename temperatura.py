# controle de temperaturas

temperatura = int(input('Digite a temperatura:'))

if temperatura < 10:
    print('Muito frio')
elif 10 <= temperatura < 20:
    print('Está fresco')
else:
    print('Está quente')