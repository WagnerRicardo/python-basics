paredeLarg = eval(input('Digite a largura da parede: '))
paredeAltu = eval(input('Digite a altura da parede: '))

paredeArea = paredeLarg * paredeAltu

litroTinta = paredeArea / 2

print(f'Para pintar essa parede será necessário {litroTinta} Litros de tinta')
