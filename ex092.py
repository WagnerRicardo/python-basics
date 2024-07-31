from datetime import date

cadastro = dict()
cadastro['Nome'] = input('Nome: ')
cadastro['Idade'] = (date.today().year - int(input('Ano de nascimento:')))
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem)'))
if cadastro['CTPS'] > 0:
    cadastro['Contratação'] = int(input('Ano de contração: '))
    cadastro['Salário'] = int(input('Salário: '))
    cadastro['Aposentadoria'] = ((cadastro['Contratação'] + 35) - date.today().year) + cadastro['Idade']
print('-='*26)
for i, k in cadastro.items():
    print(f'{i} tem valor de: {k}')
