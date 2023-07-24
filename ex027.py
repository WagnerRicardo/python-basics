nome = str(input('\033[034mDigite seu nome: ')).strip()
nomesliced = nome.split()
print(f'Primeiro nome: {nomesliced[0]}')
print(f'Último nome: {nomesliced[len(nomesliced)-1]}')
