# melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerrara quando ele disser quer mostrar 0 termos
print('Gerador de PA')
print('=-'*10)
primeiro= int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador=1
continuar=11
total=0
while continuar != 0:
    while contador <= continuar-1:
        print(f'{termo} ',' -> ' if contador <= continuar else '',end='')
        termo += razao
        contador += 1
    print('PAUSA ')
    continuar = int(input('\nQuantos termos voce quer mostrar a mais: '))
    if continuar != 0:
        continuar = contador + continuar 
        total = continuar
    else:
        break
print(f'Progressao finalizada com total de {total-1}')