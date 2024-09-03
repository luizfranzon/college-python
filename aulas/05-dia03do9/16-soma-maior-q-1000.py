# Desenvolva um programa que solicite dois números inteiros, mostre a soma destes números, e avise se a soma é maior, menor ou igual a 1000

n1 = int(input("Insira um número: "))
n2 = int(input("Insira um número: "))

total = n1 + n2

if total > 1000:
  print("Soma maior que 1000")
elif total < 1000:
  print("Menor que 1000")
else:
  print("Igual a 1000")