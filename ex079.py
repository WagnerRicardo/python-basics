lista = []
valor = 0

while True:
    while True:
        valor = input('Digite um Valor: ')
        try:
            valor = eval(valor)
            break
        except:
            print('Valor invalido, tente novamente.')
    # verificar se existe na lista
    if valor in lista:
        print('Valor Duplicado, não será adicionado.')
    else:
        lista.append(valor)

    while True:
        resp = input('Deseja continuar? S/N: ').upper()
        if resp in 'SsNn':
            break
        else:
            print('Resposta invalida, tente novamente: ')
    if resp in 'Nn':
        break
print('-='*32)
print(f'Você digitou os valores: {sorted(lista)}')
