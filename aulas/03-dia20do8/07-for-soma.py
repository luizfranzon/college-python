# Entre com 3 números, use um loop for para calcular e exibir a soma de todos os elementos

numbers = input("Insira 3 números separados por espaço: ").split(" ")
sliceFromNumber = slice(0, 3)
sumTotal = 0

for number in numbers[sliceFromNumber]:
  sumTotal += int(number)

print(f"Resultado: {sumTotal}")