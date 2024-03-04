listagem = ('Lápis', 2.00, 'Borracha', 3.00, 'Caderno', 15.00, 'Estojo', 22.50, 'Régua', 4.00
            , 'mochila', 101.00, 'Caneta', 2.00, 'Compasso', 11.99, 'Transferidor', 7.50)
print('-'*50)
print('Listagem de preços'.upper().center(64))
print('-'*50)
for i in range(0, len(listagem), 2):
    print(f'{listagem[i]:.<41}', end='R$')
    print(f'{listagem[i+1]:>7.2f}')
print('-'*50)
