import random

alunos = list()
alunos.append(input('Digite o nome do 1° aluno: '))
alunos.append(input('Digite o nome do 2° aluno: '))
alunos.append(input('Digite o nome do 3° aluno: '))
alunos.append(input('Digite o nome do 4° aluno: '))

escolhido = random.randint(0, 3)

print(f'O aluno escolhido foi {alunos[escolhido]}')
