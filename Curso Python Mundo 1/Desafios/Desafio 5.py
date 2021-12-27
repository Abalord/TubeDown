#Aula 7 desafio 5
#Faça um programa que leia um numero inteiro e mostre na tela seu antecessor e sucessor.

'''n = int(input('Digite um numero: ')) 
a = n - 1
s = n + 1
print('Analisando o valor de {}, seu antecessor e {} e o seu sucessor e {}'.format(n, a, s))'''

#solução do professor
n = int(input('Digite um numero: ')) 
print('Analisando o valor de {}, seu antecessor e {} e o seu sucessor e {}'.format(n, (n - 1), (n + 1)))