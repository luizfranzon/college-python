# 3- Soma de Números: Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero. Quando zero for inserido, o programa deve imprimir a soma total.

typedNumber = int(input("Digite um número: "))
sum = 0

while typedNumber != 0:
    sum += typedNumber
    typedNumber = int(input("Digite um número: "))

print(F"A soma total é: {sum}.")
