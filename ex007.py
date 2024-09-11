casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário: '))
anos = int(input('Em quantos anos será pago? '))
meses = anos * 12
salarioMin = (salario * 0.30) + salario

prestacaoMes = casa / meses

print(prestacaoMes)
print(salarioMin)

if (prestacaoMes < salarioMin):
    print(f'Parabéns seu valor foi aprovado, a parcela é de {prestacaoMes} durante {anos} anos')
elif (prestacaoMes > salarioMin):
    print('Desculpa, o empréstimo não pode ser aprovado')