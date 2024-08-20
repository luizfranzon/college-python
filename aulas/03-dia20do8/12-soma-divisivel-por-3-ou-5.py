# Escreva um programa que some todos os números de 1 a 50 que são divisíveis por 3 ou por 5.

for number in range(1, 50):
  if number % 3 == 0 or number % 5 == 0:
    print(number)