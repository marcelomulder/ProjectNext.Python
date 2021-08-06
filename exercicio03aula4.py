# 3 . Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
primos = [2]
verificador =  False
num = int(input("Insira um número inteiro maior que 1: "))
if num <= 1:
    print("Número inválido.")
else:
    for i in range(2,num+1):
        j = 2
        while (i % j != 0 and i >= j):
            j += 1
            if i == j:
                verificador = True
        
        if verificador == True:
            primos.append(i)
            verificador =  False 
    print(primos)