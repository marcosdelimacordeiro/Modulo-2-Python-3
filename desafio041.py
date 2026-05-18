# A Confederacao nacional de natacao precisa de um programa que leia o nascimento de um atleta e mostre sua categoria, de acordo com a idade.
"""
 - ate 9 anos: MIRIM
 - ate 14 anos:INFANTIL
 - ATE 19 ANOS: JUNIOR
 -ATE 25 ANOS: SENIOR
 - ACIMA DE 25 ANOS : MASTER
"""
import datetime
ano_atual = datetime.datetime.today().year
nascimento = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos')

if idade <= 9:
    print(f'- Ate 9 anos: MIRIM')
elif 9 < idade <= 14:
    print(f'- Ate 14 anos: INFANTIL')
elif 14 < idade <= 19:
    print(f'- Ate 19 anos: JUNIOR')
elif 19 < idade <= 25:
    print(f'- ate 25 anos: SÊNIOR')
else:
    print(f'- Acima de 25 anos: MASTER')