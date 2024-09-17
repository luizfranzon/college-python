# Desenvolva um programa para calcular e mostrar o desconto no valor de uma  compra (fornecido pelo usuário), de acordo com a tabela

valorProduto = float(input(f"Valor do produto: R$"))
desconto = 0.0

if valorProduto > 5000:
  desconto = 0.3
if valorProduto > 1000:
  desconto = 0.2
if valorProduto <= 1000:
  desconto = 0.1

print(f"Valor do desconto: {valorProduto * desconto:.2f}")