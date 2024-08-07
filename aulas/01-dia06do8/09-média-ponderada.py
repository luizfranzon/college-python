# 09. Peça ao usuário para inserir três notas e seus respectivos pesos, e calcule a média ponderada.

firstValue = float(input("- Insira o primeiro valor: "))
firstValueWeight = float(input("- Insira o peso do primeiro valor: "))

secondValue = float(input("- Insira o segundo valor: "))
secondValueWeight = float(input("- Insira o peso do segundo valor: "))

thirdValue = float(input("- Insira o terceiro valor: "))
thirdValueWeight = float(input("- Insira o peso do terceiro valor: "))

weightSumOfAllValues = firstValueWeight + secondValueWeight + thirdValueWeight
weightedAverage = ((firstValue * firstValueWeight) + (secondValue * secondValueWeight) + (thirdValue * thirdValueWeight)) / weightSumOfAllValues

print(f"Média ponderada: {weightedAverage:.2f}")