# 9- Encontrar o Menor: Crie um programa que peça ao usuário para inserir números continuamente e encontre o menor número inserido. O loop deve terminar quando o usuário digitar "parar".

typedValue = int(input('Digite um número: '))
comparator = typedValue

while typedValue != 'parar':
  typedValue = input('Digite um número: ')

  if typedValue == 'parar':
    break

  if int(typedValue) < comparator:
    comparator = int(typedValue)

print(f'O menor número digitado foi: {comparator}')
