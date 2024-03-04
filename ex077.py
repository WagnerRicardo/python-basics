lista = ('APRENDER', 'LIVRO', 'PROGRAMA', 'LINGUAGEM', 'FUTURO', 'PYTHON', 'CURSO', 'GRATIS'
         'VIDEO', 'TRABALHAR', 'PRATICAR', 'MERCADO', 'ESTUDAR', 'SOFTWARE', 'PROGRAMADOR')

for i in range(0, len(lista)):
    print(f'Na palavra {lista[i]} temos', end=' ')
    for k in range(0, len(lista[i])):
        if lista[i][k]in 'AEIOU':
            print(lista[i][k], end=' ')
    print('')
