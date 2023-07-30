num = int(input('Digite um número inteiro: '))
prime = False
divOutro = 0

for i in range(2, num + 1):
    if i != num and num % i == 0:
        divOutro = 1
    if i == num and divOutro == 0:
        prime = True
    else:
        prime = False
if prime == True:
    print(f'O número {num}, é primo!')
else:
    print(f'O número {num}, não é primo.')
