def leiaint(msg=''):
    """
        Validador de número inteiro
    :param msg: mensagem para mostrar no console
    :return: o número inteiro
    """
    n = input(msg)
    try:
        n = int(n)
    except ValueError:
        print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[0;0m')
        n = leiaint(msg)
    return n


num = leiaint('Digite um Número Inteiro: ')
print(f'Você digitou {num}')
