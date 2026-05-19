#Desenvolva um programa que leia o primeiro termo e a razao de um PA. no final, mostre os 10 primeiros termos dessa progressao
print(f'='*30)
print(f' 10 TERMOS DE UMA PA')
print(f'='*30)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
for c in range(1,11):
    an = a1 + r*(c - 1)
    print(an,end='->')
print('Acabou!!')