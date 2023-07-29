from datetime import date
birth = int(input('Digite o ano de nascimetno do atleta: '))
age = date.today().year - birth

if age <= 9:
    print('O atleta se encontra na categoria Mirim')
elif age <= 14:
    print('O atleta se encontra na categoria Intantil')
elif age <= 19:
    print('O atleta se encontra na categoria Junior')
elif age <= 25:
    print('O atleta se encontra na categoria Sênior')
else:
    print('O atleta se encontra na categoria Master')
