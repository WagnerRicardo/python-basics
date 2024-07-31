def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    resp = f'{idade} anos, Voto Opcional'
    if idade < 16:
        resp = f'{idade} anos, Não vota'
    if 18 <= idade < 65:
        resp = f'{idade} anos, Voto Obrigatório.'

    return resp


print('-'*30)
print(voto(int(input('Digite seu ano de nascimento: '))))
