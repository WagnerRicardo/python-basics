def area(L, C):
    print(f'A área de um terreno {L} x {C} é de {L*C}.')


print('     CONTROLE DE TERRENOS    ')
print('-'*32)
area(float(input('Lagura (m): ')), float(input('Comprimento (m): ')))
