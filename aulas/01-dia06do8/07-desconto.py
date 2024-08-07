# 07. Peça ao usuário para inserir o valor de um produto e a porcentagem de desconto, e calcule o valor final com desconto.

productPrice = float(input("Insira o valor do produto: "))
discountPercentage = float(input("Insira a porcentagem de desconto do produto: "))

discountedAmount = productPrice * (discountPercentage / 100)

print("---------------------------------------")
print(f"Valor do desconto: R${discountedAmount}")
print(f"Valor final do produto com o desconto: R${productPrice - discountedAmount}")