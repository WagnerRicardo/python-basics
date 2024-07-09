lista = []
tempdict = dict()
somaIdade = 0
while True:
    tempdict['Nome'] = input('Nome: ')
    tempdict['Sexo'] = input('Sexo: ')
    tempdict['Idade'] = int(input('Idade: '))
    lista.append(tempdict.copy())

    resp = input('Deseja continuar (S/N)? ')
    if resp in 'Nn':
        break
print('-='*28)
print(f'- O grupo têm {len(lista)} pessoas')
for i in lista:
    somaIdade += i['Idade']
mediaIdade = (somaIdade / len(lista))
print(f'- A média de idade é {mediaIdade}')
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
