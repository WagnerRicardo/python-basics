peso = eval(input('Qual é o seu peso em kg? '))
altura = eval(input('QUal é a sua altura em metros? '))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC é de {imc}, e está abaixo do peso')
elif imc < 25:
    print(f'Seu IMC é de {imc}, e está no peso ideal')
elif imc < 30:
    print(f'Seu IMC é de {imc}, e está em sobrepeso')
elif imc < 40:
    print(f'Seu IMC é de {imc}, e está em obesidade')
elif imc > 40:
    print(f'Seu IMC é de {imc}, e está em obesidade mórbida')
