# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a media de idade do grupo, qual e o nome do homem mais velho e quantas mulheres tem menos de 20 anos
soma_mulher=soma_idade=maior=0
nome_velho=''
for cont in range(1,5):
    nome= str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade'))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    soma_idade +=idade
    media = soma_idade / 4
    
    if idade > maior and sexo == 'm': 
        maior = idade
        nome_velho = nome
    if sexo=='f' and idade < 20:
        soma_mulher +=1


print(f'A media de idade do grupo é de {media} anos ')
print(f'O homem mais velho tem {maior} anos e se chama {nome_velho}')
print(f'Ao todo sao {soma_mulher} com menos de 20 anos de idade.')
