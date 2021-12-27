#Aula 7 desafio 6
# Crie um programa que leia um numero e mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)

#print('o dobro de {} vale {}.'.format(n, d))
print('o triplo de {} vale {}. \nA raiz quadrada de {} e igual a {:.2f}'.format(n, t, n, r))



