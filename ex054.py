from datetime import date
deMaior = 0
anoAtu = date.today().year
for i in range(0, 6):
    nasc = int(input(f'Digite o ano de nascimento da {i + 1}º Pessoa: '))
    idade = anoAtu - nasc
    if nasc > anoAtu:
        print('Ano inválido')
    else:
        if idade >= 18:
            deMaior += 1
print(f'Ao todo {deMaior} pessoas já são maior de 18 anos')
