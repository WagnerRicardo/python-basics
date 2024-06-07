lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = input(f'Digite um valor para a posição [{i}, {j}]: ')
print('-='*28)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
    print('\n')
