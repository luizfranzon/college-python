# Adivinhe o Número: Gere um número aleatório entre 1 e 100. Solicite ao usuário para adivinhar o número
import random
import math


randomNumber = math.floor(random.random() * 101)

while(True):
  guessNumber = int(input("Adivinhe o número (0-100): "))

  if guessNumber == randomNumber:
    print("Você acertou!")
    break

  if guessNumber < randomNumber:
    print("Precisa ser maior")

  if guessNumber > randomNumber:
    print("Precisa ser menor")