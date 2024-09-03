# Faça um programa que leia um caractere que representa o tipo de combustível comprado (a, d ou g) e a quantidade em litros. O programa deve imprimir o valor em reais a ser pago pelo combustível.


alcoolPrice = 3.68
dieselPrice = 5.95
gasolinaPrice = 5.87

print("A - Alcool")
print("D - Diesel")
print("G - Gasolina")
print("-------------")
gasType = input("Insira o tipo de combustivel: ").upper()
gasLitters = int(input("Quantidade de litros: "))

if gasType == "A":
  total = alcoolPrice * gasLitters
elif gasType == "D":
  total = dieselPrice * gasLitters
elif gasType == "G":
  total = gasolinaPrice * gasLitters

print(f"Total: R${total}")