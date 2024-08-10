from time import sleep


def escreva(txt, cor='default'):
    stringlen = len(txt) + 4
    print(cor + '~' * stringlen)
    print(txt.center(stringlen))
    print('~' * stringlen)
    print('\033[0;0;0m', end='')


def ajuda(comando):
    if comando.lower() == 'fim':
        global fim
        fim = True
        return
    escreva(f'Acessando manual do comando {comando}', cores['Azul'])
    sleep(.5)
    print(cores['Branco'])
    help(comando)
    print(cores['default'], end='')
    sleep(.5)


cores = {'default':'\033[0;0;0m', 'Verde': '\033[1;42m', 'Azul': '\033[1;44m',
         'Branco': '\033[1;30;47m', 'Vermelho': '\033[1;0;41m'}
fim = False
while not fim:
    escreva('Sistema de ajuda Pyhelp', cores['Verde'])
    ajuda(input('Função ou biblioteca >'))
escreva('Até logo!', cores['Vermelho'])
