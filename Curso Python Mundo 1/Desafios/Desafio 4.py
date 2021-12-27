#aula 6 Dasafio 4
#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primario
# e todas as informações possiveis sobre ele

a = input('Digite algo: ')
print('O tipo primitivo deste valor e ',type(a))
print('So tem espaços? ', a.isspace())
print('E um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiusculo ?', a.isupper())
print('Está em mainusculo ?', a.islower())
print('Está capitalizada ?', a.istitle())
