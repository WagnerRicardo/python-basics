#tabela campeonato brasileiro de futebol.
primeiros = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Red Bull Bragantino',
             'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
             'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('-='*40)
print(f'Lista dos times do brasileirão: {primeiros}')
print('-='*40)
print(f'Os 5 primeiros são{primeiros[0:5]}')
print('-='*40)
print(f'Os 4 últimos são{primeiros[16:21]}')
print('-='*40)
print(f'Times em ordem alfabetica: {sorted(primeiros)}')
print('-='*40)
print(f'O Flamengo está na {primeiros.index("Flamengo")+1}ª posição.')
print('-='*40)
