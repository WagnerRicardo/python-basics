num = eval(input('Digite um número: '))
c = num
fat = num
while c > 1:
    fat = fat * (c-1)
    c -= 1
print(f'O fatorail de {num} é {fat}')
