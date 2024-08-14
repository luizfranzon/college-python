# 5- Crie uma calculadora simples que permita ao usuário escolher uma operação (adição, subtração, multiplicação ou divisão) e dois números, e então exiba o resultado.

print("Escolha a operação")
print("1- Adição")
print("2- Substração")
print("3- Divisão")
print("4- Multiplicação")
print("-------------------")

operation = int(input("> "))

if operation not in [1, 2, 3, 4]:
  print("Operação inválida")

firstNumber = int(input("Insira o primeiro número: "))
secondNumber = int(input("Insira o segundo número: "))

if operation == 1:
  print(f"Resultado: {firstNumber + secondNumber}")

if operation == 2:
  print(f"Resultado: {firstNumber - secondNumber}")

if operation == 3:
  if secondNumber != 0:
    print(f"Resultado: {firstNumber / secondNumber}")
  else:
    print("Impossivel dividir por 0")

if operation == 4:
  print(f"Resultado: {firstNumber * secondNumber}")