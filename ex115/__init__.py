import cadastro
from time import sleep

opt = ['Ver pessoas cadastradas', 'cadastrar nova pessoa', 'Sair do sistema']
while True:
    cadastro.menu(opt)
    resp = cadastro.leiaint('Sua opção: ')-1
    if resp == 0:
        cadastro.cadastradas()
    elif resp == 1:
        cadastro.cadastrar(input('Digite o Nome: '), cadastro.leiaint('Digite a idade: '))
    elif resp == 2:
        cadastro.escreva(f'Sistema finalizado.')
        break
    else:
        print('\033[0;31mERRO! DIGITE UMA OPÇÃO VÁLIDA.\033[0;0m')
        continue
    sleep(1)
