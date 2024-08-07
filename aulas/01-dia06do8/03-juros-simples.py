# 3. Peça ao usuário para inserir o capital, a taxa de juros e o 
# tempo, e calcule o montante final usando a fórmula de juros simples.

baseAmount = float(input("Insira o valor inicial: "))
tax = float(input("Taxa em %: "))
monthsQuantity = int(input("Tempo em meses:"))

total = baseAmount + (baseAmount * (tax / 100)) * monthsQuantity
print(f"Total: R${total}")