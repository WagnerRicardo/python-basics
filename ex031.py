dist = eval(input('Qual foi a distância da viagem em km/h? '))
preco = 0.5 * dist if dist < 200 else 0.45 * dist
print(f'O total a pagar pela viagem é de {preco:.2f}R$')
