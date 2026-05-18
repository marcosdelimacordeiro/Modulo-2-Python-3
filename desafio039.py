# faca um programa que leia o ano de nascimento de um jovem e informe, de acordeo com a sua idade, se ele ainda vai se alistar ao servico militar, se e a hora exata de se alistar ou se ja passou do tempo do alistamento. seu programa tambem devera mostrar o tempo que falta ou que passo do prazo.
from datetime import date
ano_atual = date.today().year

ano_nascimento = int(input('Digite a ano do seu nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    falta = 18 - idade #verifica a idade que ainda falta para se alista
    ano_alistamento = ano_atual + falta
    print(f'Voce ainda vai se alistar, voce tem menos de 18 anos, ainda falta {falta} anos para voce poder ser alistar.')
    print(f'O seu alistamento vai ser no ano de {ano_alistamento}')
elif idade == 18:
    print(f'Voce esta na hora exata de se alistar, voce ja tem 18 anos, deve ir se alistar.')
elif idade > 18:
    anos = idade - 18
    ano_alistamento = ano_atual - anos
    print(f'Voce ja passou do prazo de se alistar em {anos} anos, deve ir se alistar mais rapido possivel.')
    print(f'O seu alistamento foi em {ano_alistamento}')
