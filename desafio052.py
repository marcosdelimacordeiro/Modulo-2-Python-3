# Faca um programa que leia um numero inteiro e dig se ele e ou nao um numero primo

num = int(input('Digite um numero: '))
cont=0
for c in range(1,num+1):
    if num % c == 0:
        cont+=1
    
if cont ==2:
    print(f'E primo')
else:
    print(f'Nao e primo!')