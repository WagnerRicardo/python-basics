lista = []
tempList = []
tempListB = []
tempVal = 0
resp = ''
while True:
    tempList.append(input('Nome: '))
    for i in range(0, 2):
        while True:
            try:
                tempVal = float(input(f'Nota {i + 1}: '))
                tempListB.append(tempVal)
                break
            except ValueError:
                print('Digite somente números')
    tempList.append(tempListB[:])
    lista.append(tempList[:])
    tempListB.clear()
    tempList.clear()
    while True:
        resp = input('Deseja continuar? (S/N): ')
        if resp in 'SsNn':
            break
        else:
            print('Resposta invalida.')
    if resp in 'Nn':
        break
print('-='*28)
print('No.  NOME', f'{"MÉDIAS":>13}')
print('-'*28)
for i in range(0, len(lista)):
    print(f'{i:<4}{lista[i][0]:<10}{((lista[i][1][0])+(lista[i][1][1]))/2:>8.2f}')
print('-'*28)
resp = 0
while resp >= 0:
    while True:
        try:
            resp = int(input('Mostrar notas de qual aluno (Números negativos para interromper)?'))
            if resp < len(lista):
                if resp >= 0:
                    print(f'As notas de {lista[resp][0]}, são {lista[resp][1]}')
                break
            else:
                print('Número de aluno não existe.')
        except ValueError:
            print('Digite somente números inteiros')
