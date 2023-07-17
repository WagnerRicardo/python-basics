from random import randint
num = int(input('Digite um número entre 0 e 5: '))
ranNum = randint(0, 5)
if num == ranNum:
    print(f'Você ganhou! o número era {ranNum}')
else:
    print(f'Você errou! o número era {ranNum}')
