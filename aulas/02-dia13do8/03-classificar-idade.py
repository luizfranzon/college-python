# 3- Peça ao usuário para inserir a idade de uma pessoa e classifique-a como "Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65+ anos).

userAge = int(input("Insira a idade do usuario: "))

if userAge <= 12:
  print("Criança")
elif userAge <= 17:
  print("Adolescente")
elif userAge < 65:
  print("Adulto ")
else:
  print("Idoso")