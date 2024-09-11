import datetime
from datetime import datetime

ano = int(input('Digite o ano de nascimento: '))
alistamento = datetime.now().year
resp = alistamento - ano
tempo = 18 - resp

if resp < 18:
    print(f'Você ainda não precisa se alistar, faltam {tempo} anos')
elif resp == 18:
    print('Esta no ano de você se alistar')
elif resp > 18:
    print(f'Já passou do seu alistamento, esta {tempo} anos atrasado')