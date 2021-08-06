# 13. Faça um programa que receba uma palavra e calcule quantas vogais (a, e, i, o, u) possui essa palavra. 
# Entre com um caractere (vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere.

cont = 0
palavra = input("\nDigite uma palavra qualquer: ")

for i in "aeiou":
    cont += palavra.count(i)

print("\nEssa palavra possui", cont,"vogais\n")

subs = input("Digite uma letra qualquer para substituir todas as vogais: ")

for j in "aeiou":
    palavra = palavra.replace(j,subs)

print(f"\nA palavra foi alterada para {palavra}\n")