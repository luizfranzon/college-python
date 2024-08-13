# 10- Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final.

price = float(input("Insira o preço do produto: "))

if price > 100:
  price -= (price / 100) * 10

print(price)