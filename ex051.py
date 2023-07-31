termoUm = eval(input('Digite o primeiro termo da PA: '))
razao = eval(input('Digite a razão da PA: '))
decimo = razao * 10 + termoUm

print('-' * 42)
print('Os dez primeiros termos dessa PA são:')
for i in range(termoUm, decimo, razao):
    print(i, end=' - ')
print('fin ')
