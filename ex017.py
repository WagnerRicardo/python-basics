import math

catetoOposto = eval(input('Digite o comprimento do cateto oposto do triângulo retangulo: '))
catetoAdj = eval(input('Digite o comprimento do cateto Adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoAdj)
print(f'A hipotenusa deste triângulo retângulo é {hipotenusa}')
