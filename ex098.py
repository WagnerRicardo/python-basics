from time import sleep

def contagem(n1, n2, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {n1} até {n2} de {passo} em {passo}')
    if n1 > n2:
        passo = int('-' + str(passo))
        n2 -= 1
    else:
        n2 += 1
    for i in range(n1, n2, passo):
        print(i, end=' ')
        sleep(.5)
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Contagem personalizada: ')
contagem(int(input(f'{"Início:":<10}')), int(input(f'{"Fim:":<10}')),
         int(input(f'{"Passo:":<10}')))
