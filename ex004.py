d = float(input('Digite a distância da viagem em km: '))

if d <= 200:
    preco = d * 0.50
    print(f'O preço da sua viagem é de {preco}')
else:
    preco = d * 0.45
    print(f'O preço da sua é de {preco}')