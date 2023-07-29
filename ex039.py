import datetime
birth = int(input('Digite o ano de seu nascimento: '))
yearCurrent = datetime.date.today().year
age = yearCurrent - birth

if age < 18:
    saldo = 18 - age
    print(f'Você ainda vai ter que se alistar. \nfaltam {saldo} anos.')
    print(f'Você vai se alistar em {yearCurrent + saldo}')
elif age == 18:
    print('Você deve se alistar.')
else:
    saldo = age - 18
    print(f'Já passou o periodo de alistamento \nVocê está {saldo} anos atrasado.')
    print(f'Você deveria ter se alistado em {yearCurrent - saldo}')
