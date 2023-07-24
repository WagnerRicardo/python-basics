vel = float(input('Qual foi a velocidade do carro em \033[1mkm/h? '))
print('='*64)
if vel > 80:
    multa = 7 * (vel - 80)
    print(f'\033[031mVocê excedeu o limite de velociade e foi multado em \033[035m{multa:.2f}R$')
else:
    print('\033[0;032mTudo dentro dos conformes.')
