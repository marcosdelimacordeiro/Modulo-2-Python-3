# Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos
print('GERADOR DE PA')
print('=-'*10)
primeiro =int(input('Digite primeiro termo: '))
razao = int(input('Digite a razao: '))

termo = primeiro
cont  = 1
continuar = 's'
while continuar != 'n' :
    continuar = str(input('Quer mostrar mais alguns termos digita [S/N]: ')).strip().lower()
    if continuar == 's': 
        valor = int(input('Digite quantos termos a mais: '))
        c = 10 + valor
        while cont <= c:
            print(f'{termo}',' -> ' if cont < c else ' ',end='')
            termo+= razao
            cont += 1 
    else:
        while cont <=10:
            print(f'{termo}',' -> ' if cont < 10 else ' ',end='')
            termo+= razao
            cont += 1 
print(' Fim!')