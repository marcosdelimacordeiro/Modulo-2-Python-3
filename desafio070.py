# Crie um programa que leia o nome e o preco de varios produtos. o programa devera perguntar se o usuario vai continuar ou nao no final:
#a) qual e o total gasto na compra
#b)quantos produtos custam mais de r$ 1000
# c) qual e o nome do produto mais barato
total_compra=valor_maior=cont=menor=0

nome_menor=''
while True:
    nome= str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preco do produto: '))
    cont += 1
    total_compra += preco
    if preco > 1000:
        valor_maior +=1
    
    if cont == 1:
        menor = preco
    else:
        if preco<menor:
            menor = preco
            nome_menor = nome

    continuar=''
    while continuar not in ('s','n'):
        continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()[0]
    if continuar == 'n':
        break

print(f'O valor total gasto em compra foi de R$ {total_compra:.2f}')
print(f'Produtos cadastrados com valor maior que R$ 1.000,00 reais foram total de {valor_maior} produtos')
print(f'O nome do produto mais barato e {nome_menor}, e o valor e de R$ {menor:.2f} reais')