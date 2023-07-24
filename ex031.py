dist = eval(input('\033[032mQual foi a distância da viagem em km/h? '))
preco = 0.5 * dist if dist < 200 else 0.45 * dist
print('\033[034m='*20)
print(f'\033[032mO total a pagar pela viagem é de \033[035m{preco:.2f}R$')
