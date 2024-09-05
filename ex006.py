salario = float(input('Digite o salário do funcionário: '))
faixa = 1250
newsalario = float

if salario > faixa:
    newsalario = salario * 0.1 + salario
    print(f'Novo salário apos reajuste de 10%: {newsalario}')
elif salario < faixa:
    newsalario = salario * 0.15 + salario
    print(f'Novo salário após reajuste de 15%: {newsalario}')