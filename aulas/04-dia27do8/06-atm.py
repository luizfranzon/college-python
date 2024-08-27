# 6- Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo.

currentBalance = 10.00

while currentBalance > 0:
    print(f'Saldo atual: R${currentBalance:.2f}')
    withdraw = float(input('Digite o valor que deseja sacar: R$'))
    currentBalance -= withdraw

print('Saldo zerado')