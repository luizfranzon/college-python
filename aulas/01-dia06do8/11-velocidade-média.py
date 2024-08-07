# 11. Peça ao usuário para inserir a distância percorrida e o tempo gasto, e calcule a velocidade média.

distanceTraveled = float(input("Insira quantos metros foram percorridos: "))
timeSpentInMinutes = float(input("Insira o tempo decorrido em minutos: "))

averageSpeedInKmPerHour = distanceTraveled / (timeSpentInMinutes / 60)

print(f"Velocidade média: {averageSpeedInKmPerHour}")