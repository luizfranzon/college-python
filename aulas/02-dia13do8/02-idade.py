# 2- Solicite a idade do usuário e informe se ele é menor de idade, maior de idade ou idoso (considerando 18 e 65 anos como limites).

age = int(input("Insira a idade do usuario: "))

if age < 18:
  print("Menor de idade")
elif age < 65:
  print("Maior de idade")
else:
  print("Idoso")