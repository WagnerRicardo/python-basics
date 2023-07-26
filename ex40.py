nota1 = eval(input('Digite a primeira nota do aluno: '))
nota2 = eval(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'A média do aluno foi {media}. \nO aluno está reprovado.')
elif media < 7:
    print(f'A média do aluno foi {media}.\nO aluno está de recuperação.')
else:
    print(f'A média do aluno foi {media}.\nO aluno foi aprovado.')
