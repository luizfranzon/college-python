# Cálculo de Hipotenusa:

import math

valorPrimeiroCatetoAoQuadrado = math.pow(float(input("Insira o valor do primeiro cateto: ")), 2)
valorSegundoCatetoAoQuadrado = math.pow(float(input("Insira o valor do segundo cateto: ")), 2)

somaDosCatetos = valorPrimeiroCatetoAoQuadrado + valorSegundoCatetoAoQuadrado

hipotenusa = math.sqrt(somaDosCatetos)

print(f"H = {hipotenusa:.3f}")