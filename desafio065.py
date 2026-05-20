# Crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao, mostre a media entre totos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
n=total=soma_valore=0
continuar ='s'
while continuar != 'n':
    if continuar == 's':
        n = int(input('Digite um valor: '))
        soma_valore += n
        total += 1
        if total == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        
    continuar = str(input('Deseja continuar [S/N]: ')).strip().lower()
    media = soma_valore / total

print(f'Voce digitou {total} numeros e a media foi de {media}')
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')