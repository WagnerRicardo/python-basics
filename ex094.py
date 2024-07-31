lista = []
tempdict = dict()
somaIdade = 0
while True:
    tempdict['Nome'] = input('Nome: ')
    while True:
        tempdict['Sexo'] = input('Sexo [M/F]: ')
        if tempdict['Sexo'] in 'MmFf':
            break
        print('ERRO, DIGITE SOMENTE "M" OU "F".')
    tempdict['Idade'] = int(input('Idade: '))
    lista.append(tempdict.copy())
    while True:
        resp = input('Deseja continuar (S/N)? ')
        if resp in 'SsNn':
            break
        print('Digite somente "S" ou "N"')
    if resp in 'Nn':
        break
print('-='*28)
print(f'- O grupo têm {len(lista)} pessoas')
for i in lista:
    somaIdade += i['Idade']
mediaIdade = (somaIdade / len(lista))
print(f'- A média de idade é {mediaIdade:.2f}')
print('- As mulheres cadastradas foram: ', end='')
for i in lista:
    if i['Sexo'] in 'Ff':
        print(f'{i["Nome"]}; ', end='')
print()
print('- Lista de pessoas que estão acima da média: ')
for i in lista:
    if i['Idade'] > mediaIdade:
        for j, k in i.items():
            print(f'{j} = {k};', end=' ')
        print()
print('Fim.')
