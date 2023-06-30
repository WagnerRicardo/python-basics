vel = float(input('Qual foi a velocidade do carro em km/h? '))
if vel > 80:
    multa = 7 * (vel - 80)
    print(f'Você excedeu o limite de velociade e foi multado em {multa:.2f}R$')
else:
    print('Tudo dentro dos conformes.')
