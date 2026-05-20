#Melhore o jogo do desafio 28 onde o computador vai "pensar" em um numero entre 0 e 10. so que agora vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.
from time import sleep
from random import randint

computador = randint(0,10)

print('=-'*30)
print('Vamos brincar de adivinhacao!!')
print('=-'*30)
sleep(1)
print('Vou pensar em um numero!!')
sleep(1)
print('=-'*30)
print('Pronto ja pensei, agora e sua Vezes')
print('=-'*30)
print('Tente adivinha qual numero eu pensei')
print('=-'*30)
numero =int(input('Digite um numero de 0 a 10'))
contador = 1
while numero != computador:
    contador+=1
    numero = int(input('Digite novamente numero de 0 a 10: '))
    if numero == computador:
        print(f'Parabens voce acertou pensamos no mesmo numero {numero}')
print(f'Voce tentou total de {contador} tentativas para acertar!')