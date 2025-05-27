# Desafio com funções

rendimento_lata = int(input('Qual é o rendimento da lata? '))
altura_parede = int(input('Qual é a altura da parede? '))
largura_parede = int(input('Qual é a largura da parede? '))

def calculo_tinta():
    area = altura_parede * largura_parede
    total = area / rendimento_lata
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()