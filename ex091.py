from random import randint
import time
jogadores = {'JOGADOR1': randint(1, 6), 'JOGADOR2': randint(1, 6),
             'JOGADOR3': randint(1, 6), 'JOGADOR4': randint(1, 6)}
colocacao = {'1ª Lugar': ['', 0], '2ª Lugar': ['', 0], '3ª Lugar': ['', 0],
             '4ª Lugar': ['', 0]}
sortedlist = sorted(jogadores.values(), reverse=True)
print('Valores sorteados: ')
for i, k in jogadores.items():
    time.sleep(1)
    print(f'    O {i}, tirou {k}')
print('Ranking dos jogadores: ')
for i in range(0, 4):
    for j in jogadores.keys():
        if jogadores.get(j) == sortedlist[i]:
            colocacao[f'{i+1}ª Lugar'] = [j, jogadores.get(j)]
            jogadores.pop(j)
            break
for i, k in colocacao.items():
    time.sleep(1)
    print(f'    {i} foi {k[0]} com {k[1]}')
