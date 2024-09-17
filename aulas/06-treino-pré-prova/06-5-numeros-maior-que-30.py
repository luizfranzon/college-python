# Escreva um algoritmo que receba 5 números e imprima quantos números  maiores que 30 foram digitados.

numbersListBiggerThan30 = []

for n in range(5):
  number = int(input(f"Insira o {n+1}° número: "))

  if number > 30:
    numbersListBiggerThan30.append(number)

print("Números digitados maiores que 30:")
for number in numbersListBiggerThan30:
  print(f"- {number}")