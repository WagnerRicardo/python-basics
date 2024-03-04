#tuplas num aleatorios
from random import randint

lista = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print('Os números sorteados foram: ', end='')
for i in range(0, 5):
    print(f'{lista[i]}', end=' ')
lista = sorted(lista)
print('')
print(f'O maior valor foi {lista[0]}')
print(f'O menor valor foi {lista[4]}')
