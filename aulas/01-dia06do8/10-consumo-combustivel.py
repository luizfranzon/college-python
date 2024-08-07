# 10. Peça ao usuário para inserir a distância percorrida e o consumo de combustível (km/l), e calcule a quantidade de combustível gasta.

commuteDistanceInKm = float(input("Insira a distancia percorrida (Km): "))
fuelConsumptionPerKm = float(input("Consumo de combustivel por Km (Km/l): "))

fuelSpentInLiters = commuteDistanceInKm / fuelConsumptionPerKm
print(f"- Combutivel gasto: {fuelSpentInLiters}")