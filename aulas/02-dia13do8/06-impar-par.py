# 6- Peça um número ao usuário e informe se ele é par ou ímpar, e se está entre 1 e 100.

number = int(input("Insira um número: "))

isBetween1and100 = False

if number > 0 and number < 100:
  isBetween1and100 = True

if number % 2 == 0:
  print("Numero par")
else:
  print("Número impar")

if isBetween1and100:
  print("Está dentro de 1 e 100")