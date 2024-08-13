# 4- Escreva um programa que receba um número e informe se ele é divisível por 3, por 5, por ambos ou por nenhum.

n1 = int(input("Insira um número: "))

if n1 % 5 == 0 or n1 % 3 == 0:
  print("Divisivel por 5 ou 2")
else:
  print("Não é divisivel")

