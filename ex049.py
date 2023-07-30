print(f'{"tabuada":=^15}')
for i in range(1, 11):
    for k in range(1, 11):
        string = str(i) + ' x ' + str(k) + ' = ' + str(i * k)
        print(f'{string:^16}')
    print('=' * 15)
