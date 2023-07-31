frase = input('Digite uma frase: ').strip().lower().replace(' ', '')
fraserev = ''

for i in range(len(frase) - 1, -1, -1):
    fraserev += frase[i]
print(f'O inverso de {frase} é {fraserev}')

if frase == fraserev:
    print(f'Essa Frase é um palíndroma!')
else:
    print(f'Essa frase não é um palíndroma.')
