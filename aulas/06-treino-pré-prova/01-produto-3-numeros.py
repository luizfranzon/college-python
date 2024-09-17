total = 0

for n in range(3):
  number = int(input(f"Insira o {n+1}° número: "))
  if total > 0:
    total *= number
  if total == 0:
    total = number
  print(total)

print(f"Total: {total}")