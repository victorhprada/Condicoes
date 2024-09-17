nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'Reprovado, média é {media:.1f}')
elif 7 > media >=5:
    print(f'Recuperação, média é {media:.1f}')
else:
    print(f'Aprovado, média é {media:.1f}')