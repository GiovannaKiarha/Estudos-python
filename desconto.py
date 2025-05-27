# desconto

compra = float(input('Digite o valor da sua compra: R$'))

if compra > 200:
    desconto = 0.2
    print('')
elif compra > 100:
    desconto = 0.1
else:
    desconto = 0.05

valor_final = compra - (compra*desconto)
print(f' O valor final com o desconto é de R$ {valor_final:.2f}')
