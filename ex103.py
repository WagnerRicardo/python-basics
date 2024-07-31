def ficha(nome, gols):
    if nome == '':
        nome = '<Desconhecido>'
    if gols == '':
        gols = 0
    else:
        int(gols)
    print(f'O jogador {nome}, fez {gols} gols(s) no campeonato.')


print('-'*23)
ficha(input('Nome do jogador: '), input('Número de gols: '))
