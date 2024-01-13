#CAIXA ELETRONICO
print('='*28)
print('Bancos CEV'.center(28))
print('='*28)
while True:
    sacar = input('Quanto você quer sacar? R$').strip()
    try:
        sacar = int(eval(sacar))
        break
    except:
        print('Digite um valor Inteiro.')
        pass
#tratamento
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0
faltam = sacar


while True:
    if faltam < 50:
        break
    faltam -= 50
    ced50 += 1
while True:
    if faltam < 20:
        break
    faltam -= 20
    ced20 += 1
while True:
    if faltam < 10:
        break
    faltam -= 10
    ced10 += 1
while True:
    if faltam == 0:
        break
    faltam -= 1
    ced1 += 1
print('=' * 50)
print(f'Total de {ced50} cédulas de R$50')
print(f'Total de {ced20} cédulas de R$20')
print(f'Total de {ced10} cédulas de R$10')
print(f'Total de {ced1} cédulas de R$1')
print('='*50, '\n Volte Sempre ao banco CEV! Tenha um bom dia.')
print('='*50)
