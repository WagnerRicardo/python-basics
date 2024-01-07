#Exercicio Produtos e preços
print('-'*32, '\n','LOJA SUPER BARATÃO'.center(30))
print('-'*32)

totGasto = 0
prodMil = 0
prodBarato = ''
prodAnterior = 0

while True:
    #CADASTRO DE PRODUTO
    produto = input('Nome do produto: ').strip()
    while True:
        valor = input('Preço: R$').strip()
        try:
            valor = eval(valor)
            break
        except:
            print('Digite um valor númerico.')
            pass
    #TRATAMENTO
    totGasto += valor
    #CONTINUAR PROGRAMA?
    while True:
        continuar = input('Quer continuar? (S/N)').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break
