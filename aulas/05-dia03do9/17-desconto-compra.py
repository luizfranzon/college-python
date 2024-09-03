# Desenvolva um programa para calcular e mostrar o desconto no valor de uma compra (fornecido pelo usuário), de acordo com a tabela:

# <= 1000 -> 10%
# >= 1000 && <= 5000 -> 20%
# > 5000 -> 30%

productValue = float(input("Insira o valor do produto: "))
totalDiscount = 0

if productValue <= 1000:
  totalDiscount = productValue * 0.10
elif productValue >= 1000 and productValue <= 5000:
  totalDiscount = productValue * 0.20
else:
  totalDiscount = productValue * 0.30

total = productValue - totalDiscount

print(f"Valor desconto: {totalDiscount}")
print(f"Total: {total}")