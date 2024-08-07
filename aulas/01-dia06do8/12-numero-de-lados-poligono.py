# 12. Peça ao usuário para inserir o número de lados de um polígono e calcule a soma dos ângulos internos.

sidesQuantity = int(input("Insira a quantidade de lados do poligono: "))

sumOfInteriorAngles = (sidesQuantity - 2) * 180

print(f"Soma dos angulos internos: {sumOfInteriorAngles}º")