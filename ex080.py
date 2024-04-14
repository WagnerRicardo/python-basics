lista = []
valor = 0
for i in range(0, 5):
    while True:
        valor = input('Digite um Valor: ')
        try:
            valor = eval(valor)
            break
        except:
            print('Valor invalido, tente novamente.')
    if i == 0:
        lista.append(valor)
        print('Valor inserido ao final da lista')
    else:
        if len(lista) > 1:
            for j in range(0, len(lista)):
                if valor <= lista[j]:
                    lista.insert(j, valor)
                    print(f'Valor inserido na posição {j}')
                    break
                if j == len(lista)-1:
                    lista.append(valor)
                    print('Valor inserido ao final da lista')
        else:
            if valor >= max(lista):
                lista.append(valor)
                print('Valor inserido ao final da lista')
            else:
                lista.insert(0, valor)
                print('Valor inserido na posição 0 da lista')
print('-='*24)
print(lista)
