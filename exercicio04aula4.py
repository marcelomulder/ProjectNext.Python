# 4. Faça um programa que calcule o mostre a média aritmética de N notas.

verificador = True
nota = soma = 0
i = 0

while verificador == True:
  nota = int(input("Informe a nota: "))
  soma += nota
  i += 1
  continua = " "
  while (continua.upper() != "S" and continua.upper() != "N"):
    continua = input("Tem mais notas para inserir? S - Sim / N - Não: ")
    if (continua.upper() != "S" and continua.upper() != "N"):
      print("Comando inválido. Tente novamente.\n")
    elif (continua.upper() == "N"):
      verificador = False

media = soma / i
print(f"A média é {round(media,2)}")