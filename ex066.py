# breaking loops
s = t = n = 0

while True:
    n = int(eval(input('Digite um número (999 para parar): ')))
    if n == 999:
        break
    s += n
    t += 1

print(f'A soma dos {t} números digitados é de: {s}')
