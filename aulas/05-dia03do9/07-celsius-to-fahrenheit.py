# Escreva um programa que converte uma temperatura de graus Celsius para Fahrenheit.

temperatureInCelsius = float(input("Insira a temperatura em Celsius: "))

temperatureInFahrenheit = (temperatureInCelsius * (9/5)) + 32

print("Valor convertido para Fahrenheit")
print(f"{temperatureInCelsius}°C -> {temperatureInFahrenheit}°F")