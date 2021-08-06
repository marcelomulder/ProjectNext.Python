# 10. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# a. Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# b. Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o 
# preço do litro da gasolina é 2.50 o preço do litro do álcool é 1,90.

tipo = (str(input("Informe o tipo de combustível (A- Álcool / G - Gasolina): "))).upper()
if (tipo != "A" and tipo != "G"):
  print("Código inválido.")
else:
  quant = float(input("\nInforme a quantidade abastecida: "))
  
  if (tipo == "A" or tipo == "a"):
    if (quant > 20):
      total = quant * 1.9 * 0.95
    else:
      total = quant * 1.9 * 0.97
  else:
    if (quant > 20):
      total = quant * 2.5 * 0.94
    else:
      total = quant * 1.9 * 0.96

  print(f"\nValor total = R$ {round(total,2)}\n")