#tuplas num aleatorios
from random import randint

lista = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os números sorteados foram: ', end='')
for i in range(0, 5):
    print(f'{lista[i]}', end=' ')
print('')
print(f'O maior valor foi {max(lista)}')
print(f'O menor valor foi {min(lista)}')
