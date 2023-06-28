nome = str(input('Digite seu nome: ')).strip()
nomesliced = nome.split()
print(f'Primeiro nome: {nomesliced[0]}')
print(f'Último nome: {nomesliced[len(nomesliced)-1]}')
