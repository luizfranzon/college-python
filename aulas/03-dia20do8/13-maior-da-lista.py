# Dada uma lista de números, use um loop for para encontrar e exibir o maior número da lista.

numberList = input("Insira uma lista de números: ").split(" ")
base = 0

for number in numberList:
  currentNumber = int(number)
  if currentNumber > base:
    base = currentNumber

print(f"Maior da lista: {base}")