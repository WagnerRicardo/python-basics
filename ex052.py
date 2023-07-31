num = int(input('Digite um número inteiro: '))
divCont = 0
print(f'O número {num} é divisivel por:')

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[32m{i}', end=' ')
        divCont += 1
if divCont == 2:
    print(f'\n\033[mO número {num}, é primo!')
else:
    print(f'\n\033[mO número {num}, não é primo.')
