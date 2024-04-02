#por extenso
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'onze', 'Doze', 'Treze', 'catorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
while True:
    resp = input('Digite um número entre 0 e 20:').strip()
    try:
        resp = eval(resp)
        if 0 <= resp <= 20:
            break
        else:
            print('Valor inválido, tente novamente. ')
    except:
        print('Valor inválido, tente novamente. ')
        pass
print(f'Você digitou o número: {extenso[resp]}')
