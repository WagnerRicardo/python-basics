opt = 0
num1 = eval(input('Digite o primeiro número: '))
num2 = eval(input('Digite o segundo número: '))
while 5 != opt:
    opt = int(input('O que deseja fazer?\n[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 '
                    '] NOVOS NÚMEROS\n[ 5 ] SAIR\n'))
    if opt == 1:
        print(f'A soma entre {num1} e {num2} é {num1 + num2}')
    elif opt == 2:
        print(f'A múltiplicação de {num1} e {num2} é {num1 * num2}')
    elif opt == 3:
        print(f'entre {num1} e {num2}, o maior número é: ', end='')
        if num1 > num2:
            print(f'{num1}.')
        else:
            print(f'{num2}')
    elif opt == 4:
        num1 = eval(input('Digite o primeiro número: '))
        num2 = eval(input('Digite o segundo número: '))
    else:
        print('Opção invalida, tente novamente.')
print('Você encerrou o programa.')
