from datetime import date
deMaior = 0
invalidos = 0
anoAtu = date.today().year
for i in range(0, 7):
    nasc = int(input(f'Digite o ano de nascimento da {i + 1}º Pessoa: '))
    idade = anoAtu - nasc
    if idade < 0 or idade > 190:
        print('Ano inválido')
        invalidos += 1
    else:
        if idade >= 18:
            deMaior += 1
print(f'Ao todo {deMaior} pessoas já são maior de 18 anos e {7 - deMaior - invalidos}'
      f' são menor de idade')
