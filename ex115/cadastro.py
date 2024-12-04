def menu(opt):
    escreva('Menu Principal')
    for i in range(0, len(opt)):
        print(f'{i + 1} - {opt[i]}')
    print('-' * 30)


def escreva(txt, cor='default'):
    print('-' * 30)
    print(txt.center(30))
    print('-' * 30)
    print('\033[0;0;0m', end='')


def leiaint(msg):
    try:
        num = input(msg)
        num = int(num)
    except (ValueError, TypeError, KeyboardInterrupt):
        print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[0;0m')
        num = leiaint(msg)
    return num


def cadastradas():
    escreva('Pessoas cadastradas')
    try:
        file = open('cadastradas.txt', 'r')
        ler = file.readlines()
    except Exception as e:
        file = open('cadastradas.txt', 'w')
        file.close()
        print('Arquivo não encontrado, criado novo arquivo .txt vazio')
    else:
        if len(ler) == 0:
            print('Ninguém foi cadastrado.')
        else:
            for i in ler:
                print(i.strip())
    file.close()


def cadastrar(Nome, Idade):
    entrada = Nome + '\t' + str(Idade) + ' anos' + '\n'
    file = open('cadastradas.txt', 'a')
    file.write(entrada)
    file.close()

