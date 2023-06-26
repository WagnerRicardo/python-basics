import random

alunos = list()
alunos.append(input('Digite o nome do 1° aluno: '))
alunos.append(input('Digite o nome do 2° aluno: '))
alunos.append(input('Digite o nome do 3° aluno: '))
alunos.append(input('Digite o nome do 4° aluno: '))

escolhido = random.choice(alunos)

print(f'O aluno escolhido foi {escolhido}')
