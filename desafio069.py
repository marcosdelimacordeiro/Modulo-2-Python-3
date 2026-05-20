# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. no final, mostre:
#a) quantas pessoas tem mais de 18 anos 
#b) quantos homens foram cadastrado
#c) quantas mulheres tem menos de 20 anos
cont_homen=cont_idade=cont_mulher=0
while True:
    print('-'*20)
    print(f'Cadastre uma Pessoa')
    print('-'*20)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in ('m','f'):
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().lower()[0]
    print('-'*20)
    
    if idade > 18:
        cont_idade += 1
    if sexo == 'm':
        cont_homen+=1   
    if sexo == 'f' and idade < 20:
        cont_mulher += 1
    continuar = ' '
    while continuar not in ('s','n'):
        continuar = str(input('Quer continuar: [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
    

print(f'''
A) Total de pessoas que tem mais de 18 anos foi de {cont_idade} 
B) Total de Homens que foram cadastrado foi de {cont_homen}
C) Mulheres que tem menos de 20 anos foi de {cont_mulher}

''')