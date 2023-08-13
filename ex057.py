valido = False

while not valido:
    sexo = input('Digite o seu sexo (M/F): ').upper()
    if sexo == 'M' or sexo == 'F':
        valido = True
print('Fim')
