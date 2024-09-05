a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a < b and a < c:
    print(f'O menor valor digitado foi: {a}')
elif b < a and b < c:
    print(f'O menor valor digitado foi: {b}')
elif c < a and c < b:
    print(f'O menor valor digitado foi: {c}')

if a > b and a > c:
    print(f'O maior valor digitado foi: {a}')
elif b > a and b > c:
    print(f'O maior valor digitado foi: {b}')
elif c > a and c > b:
    print(f'O maior valor digitado foi: {c}')