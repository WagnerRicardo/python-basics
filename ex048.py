print('= = = soma dos números ímpares múltiplos de três (um a quinhetos) = = =')
somImp = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        somImp += 1
print(f'A soma de todos impares múltiplos de três é {somImp}')
