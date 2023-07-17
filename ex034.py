salario = eval(input('Qual o salário do funcionario R$'))
aumento = 0.15
if salario > 1250:
    aumento = 0.10
salarioNovo = salario + (salario * aumento)
print(f'O aumento será de {aumento * 100}%, sendo o novo salário R${salarioNovo:.2f}')
