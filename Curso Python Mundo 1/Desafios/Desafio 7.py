#Aula 7 desafio 7
#Desenvolva um programa que leia as duas notas de um aluno e calcule a sua media

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2 #usar parenteses para forçar a orden de precedencia
print('A media entre {:.1f} e {:.1f} e {:.1f}'.format(n1, n2, m))