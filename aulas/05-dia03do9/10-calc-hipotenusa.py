# Cálculo de Hipotenusa: Usando o Teorema de Pitágoras, crie um programa que peça os comprimentos dos dois catetos de um triângulo retângulo e calcule a hipotenusa:
import math

firstCathetus = float(input("Insira o valor de um dos catetos: "))
secondCathetus = float(input("Insira o valor de outro catetos: "))

hypotenuse = math.sqrt((firstCathetus * firstCathetus) + (secondCathetus * secondCathetus))
print(f"Valor da hipotenusa: {hypotenuse:.2f}")