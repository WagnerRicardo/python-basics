nome = ['', '', '', '']
idade = ['', '', '', '']
sexo = ['', '', '', '']

idadeSoma = 0
homemVelho = 0
mulherVinte = 0

for i in range(0, 4):
    print('=' * 50)
    nome[i] = input(f'Digite o {i + 1}° nome:')
    idade[i] = int(input('Digite a idade: '))
    sexo[i] = input('Digite o sexo (H/M):').upper()

    idadeSoma += idade[i]
    if sexo[i] == 'H':
        if idade[homemVelho] < idade[i]:
            homemVelho = i
    elif sexo[i] == 'M':
        if idade[i] < 20:
            mulherVinte += 1
print('=' * 50)
print(f'\033[034mO grupo tem uma média de idade de {idadeSoma / 4:.2f}.')
print(f'\033[035mO Homem mais velho é {nome[homemVelho]}.')
print(f'\033[036mE ao todo há {mulherVinte} mulheres com menos de 20 anos.')
