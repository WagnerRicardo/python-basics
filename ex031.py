dist = eval(input('Qual foi a distância da viagem em km/h? '))
if dist < 200:
    preco = 0.5 * dist
    print(f'O total a pagar pela viagem é de {preco:.2f}R$')
else:
    preco = 0.45 * dist
    print(f'O total a pagar pela viagem é de {preco:.2f}R$')
