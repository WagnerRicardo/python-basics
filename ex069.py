# CADASTROS

maisDe18 = 0
totHomens = 0
mulherMenosDe20 = 0

while True:
    #Cadastro
    print('-'*26, '\n', 'CADASTRE UMA PESSOA'.center(26))
    print('-'*26)
    #valida idade
    idade = ''
    while not isinstance(idade, int):
        try:
            idade = eval(input('Idade: ').strip())
            break
        except:
            continue
    #valida sexo
    sexo = ''
    while sexo != 'M' or sexo != 'F':
        if sexo == 'M' or sexo == 'F':
            break
        sexo = input('Sexo [M/F]: ').upper().strip()

    #tratamento
    if idade >= 18:
        maisDe18 += 1
    if sexo == 'M':
        totHomens += 1
    if idade <= 20 and sexo == 'F':
        mulherMenosDe20 += 1
    #continuar programa ou não
    print('-' * 26)
    continuar = ''
    while continuar != 'S' or continuar != 'N':
        if continuar == 'N' or continuar == 'S':
            break
        continuar = input('Deseja continuar (S/N)? ').upper().strip()
    if continuar == 'N':
        break

print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Total de pessoas com mais de 18 anos: {maisDe18}')
print(f'Ao todo temos {totHomens} Homens cadastrados')
print(f'Ao todo temos {mulherMenosDe20} Mulheres com menos de 20 anos')
