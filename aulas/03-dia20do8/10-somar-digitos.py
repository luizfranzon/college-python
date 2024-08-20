# Escreva um programa que some os dígitos de um número inteiro fornecido pelo usuário.

number = input("Escreva um número inteiro: ")
sumTotal = 0

for digit in number:
  sumTotal += int(digit)

print(sumTotal)