# Média Aritmética: Crie um programa que solicite cinco números e calcule a média aritmética deles.

total = 0
quantity = 5

for n in range(quantity):
  number = int(input(f"Insira o {n+1}° número: "))
  total += number

average = total / quantity

print(f"Média: {average:.2f}")