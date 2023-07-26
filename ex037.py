num = int(input('Digite um número inteiro: '))
print('Escolha para qual base quer converter:')
opt = int(input('1 - Binário \n2 - para octal \n3 - para hexadecimal \n'))
if opt <= 3:
    if opt == 1:
        print(f'em Binário o número será: {(bin(num))[2:]}')
    elif opt == 2:
        print(f'em octal o número será: {(oct(num))[2:]}')
    else:
        print(f'em hexadecimal o número será: {(hex(num))[2:]}')
else:
    print('Digite um valor entre 1 e 3.')
