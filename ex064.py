num = 0
totNum = 0
somaNum = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        totNum += 1
        somaNum += num
print(f'Você digitou {totNum} números, e a soma deles é de {somaNum}')
