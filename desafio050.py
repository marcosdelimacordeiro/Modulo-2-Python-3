# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar, desconsidere-o
soma=0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos valores pares inteiros foi de {soma}')