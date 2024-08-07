# 04. Crie duas variáveis a e b, atribua valores a elas e imprima a soma, subtração, multiplicação e divisão dos valores.

a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))

print("----------------------")
print(f"Adição: {a + b:.2f}")
print(f"Subtração: {a - b:.2f}")
print(f"Multiplicação: {a * b:.2f}")
if b <= 0:
  print(f"Não é possivel dividir por 0")
else:
  print(f"Divisão: {a / b:.2f}")
print("----------------------")