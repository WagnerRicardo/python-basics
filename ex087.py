lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = col3 = 0
for i in range(0, 3):
    for j in range(0, 3):
        lista[i][j] = eval(input(f'Digite um valor para a posição [{i}, {j}]: '))
        if lista[i][j] % 2 == 0:
            par += lista[i][j]
        if j == 2:
            col3 += lista[i][j]
print('-='*28)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{lista[i][j]:^5}]', end='')
    print('\n')
print('-=' * 28)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {col3}')
print(f'O maior valor da segunda linha é {max(lista[1])}')
