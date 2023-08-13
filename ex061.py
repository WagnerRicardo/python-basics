primeiro = eval(input('Informe o primeiro termo da PA: '))
razao = eval(input('Informe a razão da PA:'))
limite = primeiro + razao * 10
c = primeiro
print('Os dez primeiros termos dessa progressão, são:')
while c < limite:
    print(c)
    c += razao
