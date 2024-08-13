# 7- Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais estão corretas.

typedUsername = input("Insira seu login: ")
typedPassword = input("Insira a senha: ")

if typedUsername == "admin" and typedPassword == "admin":
  print("Logado com sucesso")
else:
  print("Usuario ou senha incorretos")