resp = 'Y'
totNum = 0
somaNum = 0
maior = 0
menor = 0
while resp == 'Y':
    print('=' * 20)
    num = int(input('Digite um número: '))
    totNum += 1
    somaNum += num
    if menor == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resp = input('Deseja continuar?').upper()
media = somaNum / totNum
print(f'Você digitou {totNum} números, e a soma média é de {media}\nO maior número foi {maior} e o'
      f' menor foi {menor}')
