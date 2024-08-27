# 4- Encontrar o Máximo: Crie um programa que peça ao usuário para inserir números e encontre o maior número inserido. O programa deve continuar pedindo números até que o usuário digite "sair".

typedValue = input("Digite um número ou 'sair' para sair: ")
biggerNumber = 0

while typedValue != "sair":
    if int(typedValue) > biggerNumber:
        biggerNumber = int(typedValue)
    typedValue = input("Digite um número ou 'sair' para sair: ")

print(F"O maior número digitado foi: {biggerNumber}.")
