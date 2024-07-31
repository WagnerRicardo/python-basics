aproveitamento = {'Nome': input('Nome do jogador: '), 'gols': [], 'Total': 0}
resp = 0
for i in range(0, int(input(f'Quantas partidas {aproveitamento["Nome"]} Jogou? '))):
    resp = int(input(f'Quantos gols na partida {i}? '))
    aproveitamento['gols'].append(resp)
    aproveitamento['Total'] += resp
print('-='*32)
print(aproveitamento)
print('-='*32)
print(f'O jogador {aproveitamento["Nome"]} jogou {(len(aproveitamento["gols"]))} partidas')
for i in range(0, len(aproveitamento["gols"])):
    print(f'    => Na partida {i}, fez {aproveitamento["gols"][i]} gols')
print(f'Foi um total de {aproveitamento["Total"]} gols.')
