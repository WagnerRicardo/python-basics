termoUm = eval(input('Digite o primeiro termo da PA: '))
razao = eval(input('Digite a razão da PA: '))

print('Os dez primeiros termos dessa PA são:')
for i in range(termoUm, (razao * 10 + 1), razao):
    print(i)
