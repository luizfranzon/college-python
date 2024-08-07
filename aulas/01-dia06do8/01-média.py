#1. Peça ao usuário para inserir três números e calcule a média deles.

print("Insira 3 números para calcular a média entre eles")
firstNumber = int(input("Primeiro número: "))
secondtNumber = int(input("Segundo número: "))
thirdNumber = int(input("Terceiro número: "))

average = (firstNumber + secondtNumber + thirdNumber) / 3

print(f"Média: {average:.2f}")