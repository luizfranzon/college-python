# Diferença entre Dois Números: Peça ao usuário dois números e mostre a diferença entre o maior e o menor.

n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

if n1 > n2:
    biggerNumber = n1
    smallerNumber = n2
else:
    biggerNumber = n2
    smallerNumber = n1

diferenca = biggerNumber - smallerNumber

print(f"A diferença entre {biggerNumber} e {smallerNumber} é {diferenca}")
