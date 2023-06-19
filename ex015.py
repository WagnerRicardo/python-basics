kmPercorridos = eval(input('Quantos quilômetros o carro percorreu? '))
dias = eval(input('Por quantos dias o carro foi alugado: '))
preco = (dias * 60) + (kmPercorridos * 0.15)

print(f'O total a pagar pelo é de R${preco:.2f}')
