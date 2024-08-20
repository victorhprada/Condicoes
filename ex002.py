velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado')
    multa = (velocidade - 80) * 7
    print(f'O valor a pagar é {multa}')
else:
    print('Você não foi multado, parabéns')
