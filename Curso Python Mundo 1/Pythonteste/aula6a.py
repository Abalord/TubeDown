# Tipos primitivos e saidas de dados

'''n1 = int(input('Digite um valor inteiro: '))
print(type(n1))

n2 = float(input('Digite um valor de real: '))
print(type(n2))

n3 = bool(input('Digite um valor boleano (Treu ou False): '))
print(type(n3))

n4 = str(input('Digite um valor string entra aspas: '))
print(type(n4))'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 
print('A soma entre {} e {} vale'.format(n1, n2),s)

# solução do professor

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2 
print('A some entre {} e {} vale {}'.format(n1, n2, s))
