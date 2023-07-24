from random import randint
num = int(input('Digite um número entre 0 e 5: '))
print('-='*20)
ranNum = randint(0, 5)
if num == ranNum:
    print(f'\033[032mVocê ganhou! o número era {ranNum}')
else:
    print(f'\033[031mVocê errou! o número era {ranNum}')
