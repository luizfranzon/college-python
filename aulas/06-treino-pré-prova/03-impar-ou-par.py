# Número Par ou Ímpar: Peça um número inteiro ao usuário e determine se ele é par ou ímpar.

number = int(input("Insira um número inteiro: "))

if number % 2 == 0:
  print("É par")
else:
  print("Impar")