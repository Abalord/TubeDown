## Ordem de precedencia em Python
'''
1 ()
2 **
3 *///%
4 +-
'''


'''print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)'''


'''nome = input('Qual e seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))'''

'''n1 = int(input('Um Valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}'.format(n1 + n2))'''

n1 = int(input('Um Valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some e {}, o produto e {} e a divisão e {:.3f4}'.format(s, m, d), end=' ')
print('Divisão inteira {} e Potencia {}'.format(di, e))