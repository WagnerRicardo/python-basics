lista = [[], []]
valor = 0
for i in range(0, 7):
    while True:
        try:
            valor = float(input(f'Digite o {i+1}º Valor: '))
            break
        except ValueError:
            print('Digite somente números')
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-='*30)
print(f'Os valores pares foram: {sorted(lista[0])}')
print(f'Os valores impares foram: {sorted(lista[1])}')
