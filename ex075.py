tupla = (eval(input('Digite um valor:').strip()), eval(input('Digite um valor:').strip()),
         eval(input('Digite um valor:').strip()), eval(input('Digite um valor:').strip()))
par = False
print(f'Você digitou os valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if tupla.count(3) > 0:
    print(f'O valor 3 foi digitado primeiro na {tupla.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
for i in range(len(tupla)):
    if tupla[i] % 2 == 0:
        par = True
if par:
    print(f'Os valores pares são: ', end='')
    for i in range(len(tupla)):
        if tupla[i] % 2 == 0:
            print('(', tupla[i], end=' )')
else:
    print('Não há valores pares.')
