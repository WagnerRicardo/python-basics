num = eval(input('Digite o 1° número: '))
num2 = eval(input('Digite o 2° número: '))
num3 = eval(input('Digite o 3° número: '))
listaNum = [num, num2, num3]
listaNum.sort()
print(f'O \033[031mmaior\033[m número é {listaNum[2]} e o \033[032mmenor\033[m é {listaNum[0]}')
