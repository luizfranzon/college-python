# 08. Peça ao usuário para inserir o preço de um item e a quantidade comprada, e calcule o preço total.

productPrice = float(input("Insira o valor do produto: "))
purchasedQuantity = int(input("Insira a quantidade comprada: "))

totalPrice = productPrice * purchasedQuantity

print(f"Preço total: R${totalPrice}")