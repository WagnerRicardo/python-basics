expre = input('Digite uma expressão: ')
lista = []
balance = 0

for i in range(0, len(expre)):
    if expre[i] == '(':
        balance += 1
    elif expre[i] == ')':
        balance -= 1
if balance == 0:
    print('A expressão é valida')
else:
    print('A expressão é invalida')
