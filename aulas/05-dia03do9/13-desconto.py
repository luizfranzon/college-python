# # 10- Solicite o preço de um produto e aplique um desconto Exiba o valor final.

price = float(input("Insira o preço do produto: "))
discount = float(input("Insira uma porcentagem de desconto: "))

price -= price * (discount / 100)
print(f"Valor final {price}")