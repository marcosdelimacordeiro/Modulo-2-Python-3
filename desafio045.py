# crie um programa que faca o computador jogar jokenpo com voce:
from time import sleep
from random import choice
jokenpo = ['papel','tesoura','pedra']
computador = choice(jokenpo)
print('='*20)
print('Vamos jogar um GAME: Jokenpô...')
jogador = str(input('Agora e sua vez, digite entre Papel,Pedra,Tesoura. ')).strip().lower()
print(f'JO...')
sleep(1)
print('Ken...')
sleep(1)
print('Pô..')
sleep(1)
if computador == jogador:
    print(f'Deu Empate!! O computador escolheu {computador} e voce escolheu {jogador} tambem.')
elif jogador == 'papel' and computador == 'pedra':
    print(f'`Parabens voce ganhou!! o computador escolheu {computador} e voce escolheu {jogador}, a Papel ganha da Pedra.')
elif jogador == 'pedra'  and computador == 'tesoura':
    print(f'`Parabens voce ganhou!! o computador escolheu {computador} e voce escolheu {jogador}, a Pedra ganha da Tesoura.')
elif jogador == 'tesoura' and computador == 'papel':
    print(f'Parabens voce ganhou!! o computador escolheu {computador} e voce escolheu {jogador}, Tesoura ganha do papel.')
elif computador == 'papel' and jogador == 'pedra':
    print(f'`Computador venceu!! o computador escolheu {computador} e voce escolheu {jogador}, a Papel ganha da Pedra.')
elif computador == 'pedra'  and jogador == 'tesoura':
    print(f'`Computador venceu!! o computador escolheu {computador} e voce escolheu {jogador}, a Pedra ganha da Tesoura.')
elif computador == 'tesoura' and jogador == 'papel':
    print(f'Computador venceu!! o computador escolheu {computador} e voce escolheu {jogador}, Tesoura ganha do papel.')
