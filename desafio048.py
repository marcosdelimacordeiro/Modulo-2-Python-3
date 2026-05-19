# Faca um programa que calcule a soma entre todos os numeros que sao multiploes de tres e que se encontram no intervalo de 1 ate 500
cont=0
for c in range(1,501):
    if c % 3 == 0:
        cont += c
print(f'A soma entre todos os multiplos de 3 de o valor de {cont}')