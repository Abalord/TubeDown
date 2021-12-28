#Aula 7 desafio 12
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto de 5%.

preço = float(input('Qual o preço do produto R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção vai custar R${:.2f}'.format(preço, novo))
