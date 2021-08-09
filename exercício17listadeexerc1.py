# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
areapintada = float(input("Informe o tamanho da área pintada (em m2): "))
quant_lata = int(math.ceil(areapintada / 108))
quant_gal =  int(math.ceil(areapintada / 21.6))

quant_latamist = float((areapintada * 1.1) / 108)

print("\n---=== OPÇÕES DE COMPRA ===---\n")
print(f"--== APENAS LATAS ==--\n\nQuantidade de latas a serem compradas: {quant_lata}. Preço da compra: R$ {round((quant_lata * 80.00),2)}\n")
print(f"--== APENAS GALÕES ==--\n\nQuantidade de galões a serem compradas: {quant_gal}. Preço da compra: R$ {round((quant_gal * 25.00),2)}\n")
print("--== MIX PARA MENOR DESPERDÍCIO DE TINTA ==--\n")

if (int(math.ceil(areapintada * 1.1 / 108))) - quant_latamist <= 0.2:
  print("Neste caso, é mais interessante comprar apenas latas de tinta.\n")
  print(f"Quantidade de latas a serem compradas: {quant_lata}. Preço da compra: R$ {round((quant_lata * 80.00),2)}\n")
else:
  sobra = (quant_latamist - math.floor(quant_latamist)) * 18
  quant_galmist = float((sobra) / 3.6)
  print("Neste caso, é mais interessante comprar um mix de latas e galões.\n")
  print(f"Quantidade de latas a serem compradas: {math.floor(quant_latamist)}. Preço da compra: R$ {round((math.floor(quant_latamist) * 80.00),2)}\n")
  print(f"Quantidade de galões a serem compradas: {math.ceil(quant_galmist)}. Preço da compra: R$ {round((math.ceil(quant_galmist) * 25.00),2)}\n")
  print(f"Total da compra = R$ {round(((math.floor(quant_latamist) * 80.00) + (math.ceil(quant_galmist) * 25.00)),2) }\n")
