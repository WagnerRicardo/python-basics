# par ou impar

from random import randint

print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('-='*20)

jogador = 0
computador = 0
tipo = ''
s = 0
resultado = ''
totGanhos = 0

while jogador != 1:
    jogador = int(eval(input('Digite um número:')))
    tipo = str(input('Você quer ser par ou impar? (P/I): ')).upper().strip()
    if tipo != 'P' or tipo != 'I':
        print('Digite um valor valido')
        tipo = str(input('Você quer ser par ou impar? (P/I): ')).upper().strip()
    computador = randint(0, 100)
    s = jogador + computador

    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}, Total de {s}. O resultado é', end=' ')

    if s % 2 == 0:
        print('PAR.')
        resultado = 'P'
    else:
        print('IMPAR.')
        resultado = 'I'
    if tipo == resultado:
        print('VOCÊ GANHOU!')
        print('Vamos jogar novamente.')
        print('-=' * 20)
        totGanhos += 1
    else:
        print(f'VOCÊ PERDEU! VOCÊ GANHOU: {totGanhos} vezes.')
        print('-=' * 20)
        break
