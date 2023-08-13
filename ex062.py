primeiro = eval(input('Informe o primeiro termo da PA: '))
razao = eval(input('Informe a razão da PA:'))
termos = 10
ultimoTermo = primeiro
while termos != 0:
    limite = ultimoTermo + razao * termos
    c = ultimoTermo
    print(f'{termos} termos dessa progressão, são:')
    while c < limite:
        print(c)
        c += razao
    ultimoTermo = c
    termos = int(input('Quantos termos você deseja saber?'))
