# 7- Média de Notas: Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa.

sumTotal = 0
quantity = 0

typedGrade = int(input('Digite uma nota de 01 a 10: '))

sumTotal += typedGrade
quantity += 1

while typedGrade >= 0:
    typedGrade = int(input('Digite uma nota de 01 a 10: '))
    if typedGrade >= 0:
        sumTotal += typedGrade
        quantity += 1

average = sumTotal / (quantity)

print(f'A média das notas é: {average:.2f}')
