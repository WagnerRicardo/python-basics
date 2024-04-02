lista = []

for i in range(0, 5):
    lista.append(eval(input(f'DIGITE UM VALOR PARA POSIÇÃO {i}: ')))
print(f'O maior valor digitado foi {sorted(lista)[4]}, nas posições: ', end='')
for i in range(0, 5):
    if lista[i] == sorted(lista)[4]:
        print(i, end=' ')
print(f'\nO menor valor digitado foi {sorted(lista)[0]}, nas posições: ', end='')
for i in range(0, 5):
    if lista[i] == sorted(lista)[0]:
        print(i, end=' ')
