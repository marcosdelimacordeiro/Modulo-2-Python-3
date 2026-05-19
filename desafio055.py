# Faca um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor

maior =menor=0
for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da {pessoa}° pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso> maior:
            maior = peso
           
        if peso < menor:
            menor = peso
            

print(f'O maior peso {maior}')
print(f'O menor peso {menor}')