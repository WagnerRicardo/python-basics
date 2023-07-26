import datetime
birth = int(input('Digite o ano de seu nascimento: '))
yearCurrent = datetime.date.today().year
age = yearCurrent - birth

if age < 18:
    print(f'Você ainda vai ter que se alistar. \nfaltam {18 - age} anos.')
elif age == 18:
    print('Você está no periodo de alistamento.')
else:
    print(f'Já passou o periodo de alistamento \nVocê está {age - 18} anos atrasado.')
