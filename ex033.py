num = eval(input('Digite o 1° número: '))
num2 = eval(input('Digite o 2° número: '))
num3 = eval(input('Digite o 3° número: '))
listaNum = [num, num2, num3]
listaNum.sort()
print(f'O maior número é {listaNum[2]} e o menor é {listaNum[0]}')
