#desafio 112

def leiamoeda(msg):
    resp = input(msg).strip()
    if resp.count(',') == 1:
        inteiro = resp.split(',')[0]
        decimais = resp.split(',')[1]
        resp = inteiro + '.' + decimais
    try:
        resp = float(resp)
        return resp
    except ValueError:
        print('\033[0;31mERRO! VALOR INVALIDO!\033[0m ')
        resp = leiamoeda(msg)
    return resp

