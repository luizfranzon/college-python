# 8- Conversor de Moeda: Crie um programa que converta uma quantia em dólares para euros. Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0".

# 1 dolar = 0.89

currentEuroPrice = 0.89

dollarQuantity = float(input('Digite a quantidade de dólares que deseja converter para euros: $'))

while dollarQuantity != 0:
    euroQuantity = dollarQuantity * currentEuroPrice
    print(f'${dollarQuantity:.2f} equivale a €{euroQuantity:.2f}')
    dollarQuantity = float(input('Digite a quantidade de dólares que deseja converter para euros: $'))