n = int(input('Quantos elementos da sequencia fibonacci você deseja ver?'))
print(f'Os {n} elementos da fibonacci são: ')
c = 0
f1 = 0
f2 = 1
fibonacci = 1
while c < n:
    print(fibonacci)
    fibonacci = f1 + f2
    f1 = f2
    f2 = fibonacci
    c += 1
