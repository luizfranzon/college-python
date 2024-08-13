# 8- Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

studentGrade = float(input("Insira a nota do aluno: "))

if studentGrade >= 90:
  print("Nota A")
elif studentGrade >= 80:
  print("Nota B")
elif studentGrade >= 70:
  print("Nota C")
elif studentGrade >= 60:
  print("Nota D")
else:
  print("Nota F")