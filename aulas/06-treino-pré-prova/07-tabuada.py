# Faça um programa para exibir a tabuada de 0 a 9 de acordo com a entrada do usuário

targetTabuada = int(input("De qual número deseja ver a tabuada? "))

for n in range(11):
  print(f"{n}x{targetTabuada} = {n*targetTabuada}")