peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'A baixo do peso, seu imc é {imc:.2f}')
elif imc > 18.5 and imc < 25:
    print(f'Peso ideal, seu imc é {imc:.2f}')
elif imc > 25 and imc < 30:
    print(f'Sobrepeso, seu imc é {imc:.2f}')
elif imc > 30 and imc < 40:
    print(f'Obesidade, seu imc é {imc:.2f}')
elif imc > 40:
    print(f'Obesidade Mórbida, seu imc é {imc:.2f}')