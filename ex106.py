from time import sleep


def escreva(txt, cor='default'):
    if cor == 'verde':
        cor = '\033[1;42m'
    if cor == 'azul':
        cor = '\033[1;44m'
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
    escreva(f'Acessando manual do comando {comando}', 'azul')
    sleep(.5)
    print('\033[1;30;47m')
    help(comando)
    print('\033[0;0;0m', end='')


fim = False
while not fim:
    escreva('Sistema de ajuda Pyhelp', 'verde')
    ajuda(input('Função ou biblioteca >'))
