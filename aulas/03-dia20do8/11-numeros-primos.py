# Crie um programa que verifique quais números entre 1 e 20 são primos e os exiba.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for number in range(1, 20):
    if is_prime(number):
        print(number)