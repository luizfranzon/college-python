# 9- Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC) e classifique-o como "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade".

heigth = float(input("Insira a altura: "))
weigth = float(input("Insira a altura (Kg): "))

imc = weigth / (heigth * heigth)
print(f"{imc:.2f}")

if imc < 18.5:
  print("Abaixo do peso")
elif imc < 24.9:
  print("Peso normal")
elif imc < 30:
  print("Sobrepeso")
elif imc > 40:
  print("Obesidade")