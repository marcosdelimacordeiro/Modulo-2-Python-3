# crie um programa que leia o ano de nascimento de sete pessoas, no final, mostre quantas pessoas ainda nao antigirama maioridade e quantas sao de maiores.

from datetime import date

ano_atual = date.today().year
maior=menor=0
for c in range(1,8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu?: '))
    idade = ano_atual - nascimento
    if idade <18:
        menor += 1
    else:
        maior+=1

print(f'Ao todo tivemos {maior} pessoas maiores de idade\nE tambem tivemos {menor} pessoas menores de idade.')