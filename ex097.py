def escreva(txt):
    stringlen = len(txt) + 4
    print('~'*stringlen)
    print(txt.center(stringlen))
    print('~' *stringlen)


escreva(input('Qual texto deseja decorar?'))
