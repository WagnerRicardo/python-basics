from random import randint
computador = randint(0, 10)
jogador = int(input('Tente adivinhar o número inteiro que o computador pensou: '))
tentativas = 1
while jogador != computador:
    if jogador > computador:
        print('Menos . . .')
    else:
        print('Mais . . .')
    jogador = int(input('Tente adivinhar o número inteiro que o computador pensou: '))
    tentativas += 1
print(f'Você descobriu o número em {tentativas} tentativas, o número era {computador}!')
