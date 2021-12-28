#Aula 7 desafio 10
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade 
# de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma area de 2 metros quadrados.



l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a 
print('Sua parece tem a dimensão de {} x {} e sua area e de {} m2.'.format(l, a, area))
tinta = area / 2
print('Para pintar esta parede, você precisa de {} litros de tinta'.format(tinta))