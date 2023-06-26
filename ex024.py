nome = input('Qual o nome da cidade: ')
nomesplit = nome.upper().split()

if nomesplit[0] == 'SANTO':
    print('O nome da cidade começa com "SANTO"')
else:
    print('O nome NÃO começa com "SANTO"')
