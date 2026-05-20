# faca um programa que jogue par ou impar com o computador. o Jogo so sera interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
from random import randint

pc = randint(0,10)
soma=cont=0
while True:
    jogador = ' '
    while jogador not in 'pi':
        jogador = str(input('Você escolher Par ou Impar: ')).strip().lower()[0]
    n =int(input('Digite um numero: '))
    soma = n + pc 
    if jogador == 'p':
        
        if soma % 2 == 0 and jogador == 'p':
            print(f'Voce jogou {n} e o computador {pc}. Total de {soma} Deu PAR')
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total de {soma} Deu PAR')
            break
    elif jogador == 'i':
         
        if soma % 3 == 0 and jogador == 'i':
            print(f'Voce jogou {n} e o computador {pc}. Total de {soma} Deu IMPAR')
        else:
            print(f'Voce jogou {n} e o computador {pc}. Total de {soma} Deu IMPAR')
            break
    cont+=1
print(f'GAME OVER! Você venceu de {cont} vezes ')