# DESAFIO:
# Desenvolva um jogo de adivinhação onde o programa escolhe um número aleatório entre 1 e 100, e o usuário tem que adivinhar o número. Para cada palpite, o programa deve informar se o número é maior ou menor do que o palpite. Se o usuário acertar, o programa deve parabenizá-lo e mostrar quantas tentativas foram necessárias.

from random import random
import math

randomNumber = math.floor(random() * 100)
# print(randomNumber) CHEAT

guessesQuantity = 0

print("Tente adivinhar um número de 1 a 100")
while (True):
  guessedNumber = int(input("Número: "))
  guessesQuantity += 1

  if guessedNumber == randomNumber:
    print(f"Parabéns, você acertou em {guessesQuantity} tentaviva(s)")
    break
  else:
    print("Você errou! Tente novamente")