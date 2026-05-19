# crie um programa que mostre na tela todos os numeros pares que estao no intervalor entre 1 e 50
print('Lista de numeros Pares: ',end=' ')
for c in range(1,51):
    if c % 2 == 0:
        print(c,end=' ')
print('Acabou!')  