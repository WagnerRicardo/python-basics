frase = str(input('\033[1mDigite uma frase: \033[m')).strip()
print(f'Vezes em que a letra "A" aparece: {frase.upper().count("A")}')
print(f'Posição do primeiro "A": {frase.upper().find("A")+1}')
print(f'Posição do ultimo "A": {frase.upper().rfind("A")+1}')
