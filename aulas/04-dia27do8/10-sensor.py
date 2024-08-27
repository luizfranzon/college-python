# 10- Simulação de Dados de Sensor: Crie um programa que simule a leitura de dados de um sensor e continue capturando dados até que um valor fora do intervalo de operação seja detectado (por exemplo, fora de 0 a 100).

currentSensorValue = int(input('Digite o valor do sensor: '))

while currentSensorValue >= 0 and currentSensorValue <= 100:
    currentSensorValue = int(input('Digite o valor do sensor: '))

print("Valor fora do intervalo de operação detectado")