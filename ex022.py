nome = input('digite seu nome: ').strip()
nomeSemEspacos = nome.replace(' ', '')
nomeSplit = nome.split()

print(f'Nome Maiúsculas: {nome.upper()}')
print(f'Nome Minúsculas: {nome.lower()}')
print(f'Letras ao todo: {len(nomeSemEspacos)}')
print(f'Letras no primeiro nome: {len(nomeSplit[0])}')
