# Cálculo de Juros Simples: Escreva um programa que calcule o montante final após aplicar juros simples. Solicite o capital inicial, a taxa de juros (em porcentagem) e o tempo (em anos). Use a fórmula:

# M= C + (C×i×t) 
# onde:
# M é o montante final,
# C é o capital inicial,
# i é a taxa de juros (em porcentagem),
# t é o tempo (em anos).

initialAmmount = float(input("Insira o valor inicial: "))
annualFee = float(input("Valor da taxa anual: (0% a 100%) "))
timeInYears = int(input("Insira o tempo em anos: "))

finalAmmount = initialAmmount + (initialAmmount * (annualFee / 100) * timeInYears)

print(f"R${initialAmmount:.2f} com uma taxa de {annualFee}% ao ano, durante {timeInYears} anos = R${finalAmmount:.2f}")