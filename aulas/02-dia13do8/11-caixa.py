# 11- Desenvolva um programa que permita ao usuário escolher uma operação (saque, depósito) e simule o comportamento de um caixa eletrônico com validações básicas (ex.: saldo insuficiente para saque).

currentBalance = 0.00

print(f"Saldo atual: R${currentBalance:.2f}")
print("Escolha a operação: ")
print("1- Saque")
print("2- Deposito")
print("--------------------")

option = int(input("> "))

if option == 1:
  valueToRemove = float(input("Quanto deseja sacar: "))
  if valueToRemove <= currentBalance:
    currentBalance -= valueToRemove
  else:
    print("Saldo insuficiente")

if option == 2:
  valueToAdd = float(input("Quanto deseja depositar: "))
  currentBalance += valueToAdd