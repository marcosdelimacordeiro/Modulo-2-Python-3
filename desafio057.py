# Faca um programa que leia o sexo de uma pessoa, mas so aceite valores M ou F, caso esteja errado, peca a digitacao novamente ate ter um valor correto

sexo = str(input('Digite sexo [M/F]')).strip().lower()[0]

while sexo not in ('m','f'):
    sexo = str(input('valor invalido. Digite seu sexo novamente: [M/F] ')).strip().lower()[0]
print('Sexo registrado com sucesso\nFIM')