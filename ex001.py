import random

n = [0, 1, 2, 3, 4, 5]

resp = int(input('Digite um número de 0 a 5: '))

if resp == random.choice(n):
    print('Processando...')
    print(f'Parabéns você acertou o número pensando')
else:
    print(f'Você não acertou')