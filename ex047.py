print('NÚMEROS PARES ENTRE 1 E 50:')
totPar = 0
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        totPar += 1
print(f'No total são {totPar}')
