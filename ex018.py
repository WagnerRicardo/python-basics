import math

angle = eval(input('Digite o valor do ângulo:'))
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print(f'O seno de {angle}° é {sen:.2f}')
print(f'O cosseno de {angle}° é {cos:.2f}')
print(f'A tangente de {angle}° é {tan:.2f}')
