# faca um programa que leia um numero qualquer e mostre o seu fatorial

numero = int(input('Digite um valor para fatorial: '))

fat = 1
while numero > 0:
    fat = fat * numero
    print(f'{numero} ',end='')
    print(f' x 'if numero > 1 else ' = ',end='') # se numero for maior q 1 ele vai imprimier x , senao vai imprimir =
    numero = numero -1 

print(fat)