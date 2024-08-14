# 1- Receba dois números do usuário e mostre qual deles é o maior.

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

if n1 > n2:
  print(f"{n1} é o maior número")
elif n2 > n1:
  print(f"{n2} é o maior número")
else:
  print("Números iguais")