print('= = = soma dos números ímpares múltiplos de três (um a quinhetos) = = =  ')
somaMultiplos = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        somaMultiplos += i
        cont += 1
print(f'A soma de todos impares múltiplos de três é {somaMultiplos}, e são {cont} números.')
