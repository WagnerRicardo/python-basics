import random
print('-=-JOKENPÔ-=-')
cont = 'y'
while cont == 'y':
    jogador = int(input('Escolha um digitando o número!:\n1 - pedra\n2 - papel\n3 - tesoura\n'))
    computador = random.randint(0, 2)
    #1 pedra 2 papel 3 tesoura
    escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
    #escolha valida pelo jogador?
    if jogador <= 3:
        if jogador == 1 and computador == 1:
            print(f'O computador escolheu {escolhas[computador]}, Você perdeu!')
        elif jogador == 2 and computador == 2:
            print(f'O computador escolheu {escolhas[computador]}, você perdeu!')
        elif jogador == 3 and computador == 0:
            print(f'O computador escolheu {escolhas[computador]}, você perdeu!')
        elif jogador == (computador + 1):
            print(f'O computador escolheu {escolhas[computador]}, Empatou!')
        else:
            print(f'O computador escolheu {escolhas[computador]}, você ganhou!')
    else:
        print('Escolha inválida!')
    cont = str(input('Continuar? y/n: '))
