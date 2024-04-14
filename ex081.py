lista = []
resp = ''
valor = ''

while True:
    while True:
        valor = input('Digite um valor: ')
        try:
            float(valor)
            lista.append(valor)
            break
        except ValueError:
            print('Valor invalido!')
    while True:
        resp = input('Deseja continuar? S/N:')
        if resp in 'SsNn':
            break
        else:
            print('Valor invalido')
    if resp in 'Nn':
        break
print(f'foram digitados {len(lista)} números')
print('Em ordem decrescente os valores são:', end=' ')
for i in range(len(lista), 0, -1):
    print(sorted(lista)[i-1], end=' ')
if lista.count('5') >= 1:
    print('\nO número 5 está na lista.')
else:
    print('\nO número 5 não está na lista.')
