num = int(input('Digite um número: '))
if num%2 == 0:
    print(f'O número {num} é \033[032mpar')
else:
    print(f'O número {num} é \033[031mimpar')
