def ficha(nome, gols):
    if nome == '':
        nome = '<Desconhecido>'
    try:
        int(gols)
    except ValueError:
        gols = 0
    print(f'O jogador {nome}, fez {gols} gols(s) no campeonato.')


print('-'*23)
ficha(input('Nome do jogador: ').strip(), input('Número de gols: ').strip())
