#Aula 7 desafio 12
#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.

salario = float(input("Qual o seu salario atual R$"))
novo_salario = salario(salario * 15 / 100)
print("O salario de R${} com aumento de 15% passou a ser de R${}".format(salario, novo_salario))
