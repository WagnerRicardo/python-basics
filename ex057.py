sexo = input('Digite o seu sexo (M/F): ').strip().upper()[0]
while sexo not in 'MF':
    print('Dados invalidos.')
    sexo = input('Digite o seu sexo (M/F): ').strip().upper()[0]
print('Fim')
