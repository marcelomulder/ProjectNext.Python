# 11. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# a. par ou ímpar;
# b. positivo ou negativo;
# c. inteiro ou decimal.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe um outro número: "))
opera = (str(input("Qual operação deseja fazer? (A) Adição, (S) Subtração, (M) Multiplicação, (D) Divisão: "))).upper()

# Escolha da operação

if (opera != "A" and opera != "S" and opera != "M" and opera != "D"):
  print("Operação inválida.")
else:
  if opera == "A":
    result = num1 + num2
  elif opera == "S":
    result = num1 - num2
  elif opera == "M":
    result = num1 * num2
  else:
    result = num1 / num2

  print(f"O resultado é {result}")

  # Se é par ou impar
  if result % 2 == 0:
    print("Ele é par.")
  else:
    print("Ele é impar.")

  # Se é positivo ou negativo
  if result > 0:
    print("Ele é positivo.")
  elif result < 0:
    print("Ele é negativo.")
  else:
    print("Ele é nulo.")

  # Se é inteiro ou decimal
  if result % 1 == 0:
    print("Ele é inteiro.\n")
  else:
    print("Ele é decimal.\n")

