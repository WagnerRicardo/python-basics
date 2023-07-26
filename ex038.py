num1 = int(input('Digite o 1º número inteiro: '))
num2 = int(input('Digite o 2º número inteiro: '))

if num1 > num2:
    print(f'O 1° número ({num1}) é o maior.')
elif num2 > num1:
    print(f'O 2° número ({num2}) é o maior.')
else:
    print(f'Não há número maior, os dois números são iguais a {num1}')
