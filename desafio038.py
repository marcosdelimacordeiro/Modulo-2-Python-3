# Escreva um programa que leia dois numeros inteiros e compare-os. mostrando na tela um mensagem: - o primeiro valor e maior
# - o segundo valor e maior
#- nao existe valor maior, os dois sao iguais

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O primeiro valor e Maior!')
elif n2 > n1:
    print(f'O segundo valor e o maior!')
else:
    print('Não existe valor maior, os dois sao iguais')