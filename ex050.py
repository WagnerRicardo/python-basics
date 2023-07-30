somaPar = 0
for i in range(0, 6):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        somaPar += num
print(f'A soma de todos os números pares digitados foi {somaPar}')
