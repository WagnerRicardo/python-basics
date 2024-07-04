from datetime import date

cadastro = dict()
cadastro['Nome'] = input('Nome: ')
cadastro['Idade'] = (date.today().year - int(input('Ano de nascimento:')))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem)'))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contração: '))
    cadastro['Salário'] = int(input('Salário: '))
    contribuidos = (date.today().year - cadastro.get('Contratação'))
    cadastro['Aposentadoria'] = (date.today().year + (35 - contribuidos))
print('-='*26)
for i, k in cadastro.items():
    print(f'{i} tem valor de: {k}')
