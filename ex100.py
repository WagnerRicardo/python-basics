from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ')
    for i in range(0, 5):
        val = randint(0, 11)
        print(f'{val}', end=' ')
        sleep(.3)
        lista.append(val)
    print('Pronto! ')
    sleep(.3)


def somaPar(lista):
    par = 0
    print(f'Somando os valores pares de {lista}, temos:', end=' ')
    for i in lista:
        if (i % 2) == 0:
            par += i
    print(par)


lista = []

sorteia(lista)
somaPar(lista)
