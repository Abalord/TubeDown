#Aula 7 desafio 10
#Crie um programa que leia quanto dinheiro você tem na carteira e mostre quantos dolares ele pode comprar.

real = float(input('Quanto de dinheiro você tem na carteira R$'))
dolar = real / 5.64
print('com R${:.2f} você compra US${:.2f} dolares'.format(real, dolar))
