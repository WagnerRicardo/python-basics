frase = input('Digite uma frase: ')
frase = frase.strip()
frase = frase.lower()
frase = frase.replace(' ', '')

fraserev = ''

for i in range(len(frase) - 1, -1, -1):
    fraserev += frase[i]

if frase == fraserev:
    print(f'Essa Frase é um palíndroma!')
else:
    print(f'Essa frase não é um palíndroma.')
