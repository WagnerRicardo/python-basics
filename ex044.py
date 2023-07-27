prod = eval(input('Qual o valor do produto? R$'))
pagamento = int(input('Qual será a forma de pagamento?\n1 - Á vista no dinhero/cheque\n'
                      '2 - Á vista no cartão\n3 - Parcelado\n'))
#Formas de pagamento escolhidas
if pagamento == 1: #dinheiro a vista
    print(f'Você tem 10% de desconto, o total será de R${prod - (prod * 0.1)}')
elif pagamento == 2: #cartão á vista
    print(f'Você tem 5% de desconto, o total será de R${prod - (prod * 0.05)}')
elif pagamento == 3:
    #parcelado
    parcela = int(input('Em quantas vezes você deseja parcelar? '))
    if parcela == 2:
        print(f'Não será aplicado juros, sendo cada parcela R${prod/parcela}, e um total de R$'
              f'{prod}')
    elif parcela > 2: #condição de juros
        prod = prod + (prod * 0.2)
        print(f'Será aplicado juros de 20%, cada parcela será de R${prod/parcela}, e um total'
              f'de {prod}')
    else:
        print('Opção inválida.')

else:
    print('Opção inválida.')
