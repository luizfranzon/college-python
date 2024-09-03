# Ano Bissexto: Peça um ano ao usuário e determine se ele é um ano bissexto. (Dica: Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400).

year = int(input("Insira um ano: "))

if year % 4 == 0:
  print("Ano bissexto")
else:
  print("Näo é bissexto")