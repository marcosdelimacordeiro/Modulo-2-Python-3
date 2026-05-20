#Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de fibonacci

print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
termo = int(input('Quantos termos voce quer mostrar? '))
n1=0
n2=1
c=3
print('~'*30)
print(f'{n1} -> {n2} -> ',end='')
while c <= termo:
    n3 = n1 + n2
    print(n3,' -> ',end=' ')
    n1 = n2
    n2 = n3
    c+=1
print('FIM')
print('~'*30)