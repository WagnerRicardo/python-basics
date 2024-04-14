expre = input('Digite uma expressão: ')
lista = []

for i in range(0, len(expre)):
    if expre[i] in '()':
        lista.append(expre[i])

if (lista.count('(')) == (lista.count(')')):
    print('A expressão é valida')
else:
    print('A expressão é invalida')
