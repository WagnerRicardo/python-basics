import datetime
birth = int(input('Digite o ano de nascimetno do atleta: '))
age = datetime.date.today().year - birth

if age <= 9:
    print('O atleta se encontra na categoria Mirim')
elif age <= 14:
    print('O atleta se encontra na categoria Intantil')
elif age <= 19:
    print('O atleta se encontra na categoria Junior')
elif age <= 20:
    print('O atleta se encontra na categoria Sênior')
else:
    print('O atleta se encontra na categoria Master')
