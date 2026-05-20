# Refaca o DESAFIO 51, lendo o primeiro termo e a razao de um PA, mostrando os 10 primeiros termos da progressao usando estrutura while

a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
c=1
while c < 11:
    an = a1 + r*(c - 1)
    print(an,end=' '' -> ' if c < 10 else '')
    c+=1
print(' Fim!')