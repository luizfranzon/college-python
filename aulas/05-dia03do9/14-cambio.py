# . Conversão de Moedas: Peça ao usuário um valor em reais e a taxa de câmbio para dólares americanos. Converta o valor para dólares.

ammountInReais = float(input("Valor de reais: R$"))
dollarPrice = 5.65

total = ammountInReais / dollarPrice

print(f"Total: ${total:.2f}")
