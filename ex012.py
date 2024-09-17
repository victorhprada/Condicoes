valor = float(input('Qual o valor do produto: '))

vista = valor - (valor * 0.1)
cartao = valor - (valor * 0.05)
parcelado = valor + (valor * 0.2)

print(f'Condições de pagamento do produto no valor de R$ {valor}')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x no cartão')
opcao = int(input('Digite a opção: '))

if opcao == 1:
    print(f'Valor a ser pago no dinheiro á vista é R${vista:.2f}')
elif opcao == 2:
    print(f'Valor a ser pago no cartão á vista é R${cartao:.2f}')
elif opcao == 3:
    print(f'Valor a ser pago em até 2x no cartão {valor}')
elif opcao == 4:
    print(f'Valor a ser pago no cartão é R${parcelado:.2f}')
else:
    print('Digite uma opção válida')
