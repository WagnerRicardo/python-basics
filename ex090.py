boletim = dict()

boletim['Nome'] = input('Qual o nome do aluno(a)? ')
boletim['Média'] = float(input('qual é a média no aluno?'))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
for i, k in boletim.items():
    print(f'{i} é igual a {k}')
