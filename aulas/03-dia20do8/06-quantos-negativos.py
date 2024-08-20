# Dada uma lista de números, conte quantos números são negativos e exiba o resultado.

numberList = input("Insira uma lista de números: ").split(" ")
howManyNegative = 0

for number in numberList:
  if int(number) < 0:
    howManyNegative += 1

print(f"Negativos: {howManyNegative}")