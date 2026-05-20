# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa sera interrompido quando o numero solicitado for negativos

while True:
    n = int(input('Quer ver a tabuada de qual valor:  '))
    if n < 0:
        break
    for c in range(0,11):
        print(f'{n} X {c} = {n*c}')
    
print(f'Acabou!!')