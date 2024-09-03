# Média Aritmética: Crie um programa que solicite cinco números e calcule a média aritmética deles.

soma = 0
numbersList = []
for n in range(1, 6):
  number = int(input(f"Insira o {n}° número: "))
  numbersList.append(number)

for number in numbersList:
  soma += number

total = soma / 5

print(f"Média: {total}")