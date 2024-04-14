lista = []
par = []
impar = []
valor = ''
resp = ''

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
        resp = input('Deseja continuar (S/N)?')
        if resp in 'SsNn':
            break
        else:
            print('Valor invalido!')
    if resp in 'Nn':
        break
print('-='*30)
print(f'A lista completa é {lista}')
for i in range(0, len(lista)):
    if float(lista[i]) % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
if len(par) > 0:
    print(f'Os valores pares são {par}')
else:
    print('Não existem valores pares na lista!')
if len(impar) > 0:
    print(f'Os valores impares são {impar}')
else:
    print('Não existem valores impares na lista!')
