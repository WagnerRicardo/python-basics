num = eval(input('Digite um número: '))
c = num
fat = 1
print(f'O fatorial de {num} é: ', end='')
while c > 1:
    print(f'{c} x ', end='')
    fat *= c
    c -= 1
print(f'1 = \033[034m{fat}')
