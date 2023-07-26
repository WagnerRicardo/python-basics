# dados principais
houseVal = eval(input('Qual é o valor da casa? R$'))
salary = eval(input('Qual é o salário do comprador? R$'))
years = int(input('Em quantos anos pretende pagar?'))
# parcela calculo
installment = houseVal/(years * 12)
print(f'O valor das parcelas será de R${installment:.2f}')
# condição de aprovação para emprestimo
if (installment > (salary * 0.3)):
    print(f'Emprestimo negado pois o valor excede 30% do salário que é R${(salary * 0.3)}.')
else:
    print(f'Emprestimo aprovado.')
