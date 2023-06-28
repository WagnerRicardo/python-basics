frase = str(input('Digite uma frase: ')).strip()
print(f'Vezes em que a letra "A" aparece: {frase.upper().count("A")}')
print(f'Posição do primeiro "A": {frase.upper().find("A")+1}')
print(f'Posição do ultimo "A": {frase.upper().rfind("A")+1}')
