precoProd = eval(input('Qual o preço do produto? R$ '))
desconto = 0.05
descontoAplic = precoProd - (precoProd*0.05)
print(f'Com {desconto*100}% de desconto, O valor do produto será de R$ {descontoAplic}')
