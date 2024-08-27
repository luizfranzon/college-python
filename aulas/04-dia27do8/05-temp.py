# 5- Conversão de Temperatura: Faça um programa que converta uma temperatura de Celsius para Fahrenheit. Continue pedindo ao usuário para inserir uma nova temperatura em Celsius até que ele digite "sair".

import math

typedValue = input("Digite uma temperatura em Celsius ou 'sair' para sair: ")

while typedValue != "sair":
    celsius = float(typedValue)
    fahrenheit = celsius * 1.8 + 32
    print(F"A temperatura em Fahrenheit é: {math.floor(fahrenheit)}.")
    typedValue = input("Digite uma temperatura em Celsius ou 'sair' para sair: ")