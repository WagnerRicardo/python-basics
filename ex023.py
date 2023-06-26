num = input('Digite um número entre 0 e 9999: ')
if len(num) >= 5:
    print('Número Inválido')
else:
    while len(num) < 4:
        num = '0' + num
    print(f'Unidade: {num[3]}')
    print(f'Dezena: {num[2]}')
    print(f'Centena: {num[1]}')
    print(f'Milhar: {num[0]}')
