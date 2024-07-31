lista = []
tempdict = dict()

while True:
    print('-'*32)
    tempdict['Nome'] = input('Nome do jogador: ')
    tempdict['Gols'] = []
    tempdict['Total'] = 0
    for i in range(0, int(input(f'Quantas partidas {tempdict["Nome"]} jogou?'))):
        gol = int(input(f'Quantos gols na partida {i}? '))
        tempdict['Gols'].append(gol)
        tempdict['Total'] += gol
    lista.append(tempdict.copy())
    tempdict.clear()
    while True:
        resp = input('Deseja continuar?')
        if resp in 'SsNn':
            break
        print('Digite somente "S" ou "N"')
    if resp in 'Nn':
        break
print('-='*32)
print(f'{"Cod":<4}{"Nome":<13}{"Gols":<16}{"Total":>7}')
for i in range(0, len(lista)):
    print(f'{f"{i}":>3}', f'{lista[i]["Nome"]}'.ljust(12), f'{lista[i]["Gols"]}'.ljust(16),
          f' {lista[i]["Total"]}')
while True:
    jogador = int(input("Mostrar dados de qual jogador (Número negativo para parar)?"))
    if jogador < 0:
        print('Fim.')
        break
    if jogador >= len(lista):
        print('Código inexistente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[jogador]["Nome"]}')
        for i in range(0, len(lista[jogador]['Gols'])):
            print(f'    No jogo {i} fez {lista[jogador]["Gols"][i]} Gols.')
