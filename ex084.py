lista = []
temp = []
listaMaior = []
listaMenor = []
cont = 'n'
maior = menor = 0
while True:
    print('-='*32)
    temp.append(input('Digite o Nome da pessoa: '))
    while True:
        try:
            temp.append(float(input('Digite o peso da pessoa: ')))
            break
        except ValueError:
            print('Digite somente números')
    lista.append(temp[:])
    temp.clear()
    cont = input('Deseja continuar? S/N')
    if cont in 'Nn':
        break
for i in range(0, len(lista)):
    if i == 0:
        maior = menor = lista[0][1]
    if i > 0:
        if maior <= lista[i][1]:
            maior = lista[i][1]
        if menor > lista[i][1]:
            menor = lista[i][1]
for i in range(0, len(lista)):
    if lista[i][1] == maior:
        listaMaior.append(lista[i][0])
    if lista[i][1] == menor:
        listaMenor.append(lista[i][0])
print('-='*32)
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi {maior}, Peso de {listaMaior}')
print(f'O menor peso foi {menor}, Peso de {listaMenor}')
print('-='*32)
