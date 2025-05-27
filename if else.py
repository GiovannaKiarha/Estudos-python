# Desafio com Else, Elif e Else

ponto_carne = int(input('Digite a temperatura da carne em Celsius: '))

if ponto_carne < 48:
    print('A carne precisa cozinha por mais tempo')
if ponto_carne in range (48, 53): # também poderia ser >= mas in range melhora a visualização do código e a sintaxe
    print('A carne está selada')
elif ponto_carne in range (54, 59):
    print('A carne está ao ponto para o mal passado')
elif ponto_carne in range (60, 64):
    print('A carne está ao ponto')
elif ponto_carne in range (65, 70):
    print('A carne está ao ponto para bem')
elif ponto_carne >= 71:
    print('A carne está bem passada')
else:
    print('A carne não está própria para consumo')
