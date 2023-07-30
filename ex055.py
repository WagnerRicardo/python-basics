maior = 0
menor = 0
for i in range(0, 5):
    peso = eval(input(f'Digite o peso da {i + 1}º pessoa: '))
    if i == 0:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso registrado foi {maior:.2f}KG, e o menor foi {menor:.2f}KG')
