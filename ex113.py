def leiaint(msg):
    try:
        num = input(msg)
        num = int(num)
    except (ValueError, TypeError):
        print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[0;0m')
        num = leiaint(msg)
    except KeyboardInterrupt:
        print('\033[0;31mUsuário prefiriu não digitar este número.\033[0;0m')
        return 0
    return num


def leiafloat(msg):
    try:
        num = input(msg)
        num = float(num)
    except (ValueError, TypeError):
        print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO.\033[0;0m')
        num = leiaint(msg)
    except KeyboardInterrupt:
        print('\033[0;31mUsuário prefiriu não digitar este número.\033[0;0m')
        return 0
    return num


i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O valor inteiro foi {i}, e o valor real foi {r}')
