# Dada uma lista de números, crie um programa que multiplique todos os elementos da lista por um número fornecido pelo usuário.

numberList = input("Insira uma lista de números: ").split(" ")
multiplier = int(input("Por qual número deseja multiplicar a lista: "))

for number in numberList:
  print(f"{number}x{multiplier} = {int(number) * multiplier}")