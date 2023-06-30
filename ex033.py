num = eval(input('Digite o 1° número: '))
num2 = eval(input('Digite o 2° número: '))
num3 = eval(input('Digite o 3° número: '))
if num > num2 and num > num3:
    print(f'O maior número é o primeiro: {num}')
elif num2 > num3:
    print(f'O maior número é o segundo: {num2}')
else:
    print(f'O maior número é o terceiro: {num3}')
