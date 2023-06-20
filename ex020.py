import random

alunos = list()
alunos.append(input('Digite o nome do 1° aluno: '))
alunos.append(input('Digite o nome do 2° aluno: '))
alunos.append(input('Digite o nome do 3° aluno: '))
alunos.append(input('Digite o nome do 4° aluno: '))

random.shuffle(alunos)

print(f'O primeiro aluno a apresentar é {alunos[0]}')
print(f'O segundo aluno a apresentar é {alunos[1]}')
print(f'O terceiro aluno a apresentar é {alunos[2]}')
print(f'O quarto aluno a apresentar é {alunos[3]}')
