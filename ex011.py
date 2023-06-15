paredeLarg = eval(input('Digite a largura da parede: '))
paredeAltu = eval(input('Digite a altura da parede: '))

paredeArea = paredeLarg * paredeAltu

litroTinta = 2**2

print(f'Para pintar essa parede será necessário {paredeArea/litroTinta} Litros de tinta')
