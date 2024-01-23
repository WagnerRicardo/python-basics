#Exercicio Produtos e preços
print('-'*32, '\n','LOJA SUPER BARATÃO'.center(30))
print('-'*32)

totGasto = prodMil = 0
prodBarato = ''
prodBaratoVal = 0
lista = []
quantidade = 0

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
    #lista
    quantidade += 1
    lista.append([valor, produto])
    #TRATAMENTO
    totGasto += valor
    if valor > 1000:
        prodMil += 1

    for i in range(0, quantidade):
        if i > 0:
            if lista[i][0] < lista[i - 1][0]:
                prodBarato = lista[i][1]
                prodBaratoVal = lista[i][0]
        else:
            prodBarato = lista[i][1]
            prodBaratoVal = lista[i][0]

    #CONTINUAR PROGRAMA?
    while True:
        continuar = input('Quer continuar? (S/N)').strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
    if continuar == 'N':
        break

print('-'*10, 'FIM DO PROGRAMA','-'*10)
print(f'O Total da compra foi R${totGasto:.2f}')
print(f'Temos {prodMil} Produtos acima de R$1000,00')
print(f'O produto mais barato foi {prodBarato} no valor de R${prodBaratoVal:.2f}')
