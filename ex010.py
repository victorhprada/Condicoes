from datetime import datetime

ano = int(input('Digite o ano de nascimento do atleta: '))
inscricao = datetime.now().year
resp = inscricao - ano


if resp <= 9:
    print(f'Mirim, idade {resp}')
elif 9 < resp <=14:
    print(f'Infantil, idade {resp}')
elif 14 < resp <= 19:
    print(f'Sênior, idade {resp}')
else:
    print(f'Master, idade {resp}')