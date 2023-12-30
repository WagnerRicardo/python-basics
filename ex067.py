# tabuada
n = 0

while True:
    n = eval(input('Quer ver a tabuada de qual número (digite um número negativo para encerrar)? '))
    if n < 0:
        break
    print('-'*20)
    for i in range (1, 11):
        print(f'{n} x {i} = {(n * i)}')
    print('-'*20)

print('Programa finalizado!')
