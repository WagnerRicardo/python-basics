from random import randint
import time

lista = []
templist = []
jogos = 0
ranNum = 0

print('-'*30)
print('MEGA PALPITES'.center(30))
print('-'*30)
while True:
    try:
        jogos = int(input('Quantos jogos devo sortear? '))
        break
    except ValueError:
        print('Digite somente números inteiros')
print('-='*4, f'Sorteando {jogos} jogos', '-='*4)
for i in range(0, jogos):
    for j in range(0, 6):
        ranNum = randint(0, 60)
        if j == 0:
            templist.append(ranNum)
        else:
            while True:
                if ranNum in templist:
                    ranNum = randint(0, 60)
                else:
                    templist.append(ranNum)
                    break
    lista.append(templist[:])
    templist.clear()
for i in range (0, jogos):
    print(f'Jogo {i+1}: {sorted(lista[i])}')
    time.sleep(.7)
print('-='*5, '< Boa sorte! >', '-='*5)
