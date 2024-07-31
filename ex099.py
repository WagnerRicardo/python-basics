from time import sleep

def maior(* num):
    print('-='*25)
    print('Analisando os valores passados . . .')
    maximo = 0
    for i in num:
        print(i, end=' ')
        sleep(.5)
        if i > maximo:
            maximo = i
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maximo}.')


maior(1, 2)
maior(1, 2, 5, 5, 3, 67)
maior(5, 7, 23, 4)
maior()
