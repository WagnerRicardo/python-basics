r1 = eval(input('Digite o comprimento da 1° reta: '))
r2 = eval(input('Digite o comprimento da 2° reta: '))
r3 = eval(input('Digite o comprimento da 3° reta: '))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3:
    print('\033[32mEssas retas podem formar um triângulo.')
else:
    print('\033[31mEssas retas não podem formar um triângulo')
