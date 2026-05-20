# Crie um programa que leia varios numeros inteiros pelo teclado.O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. no final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag).
n=soma=total=0
while n != 999:
    n=int(input('Digite um valor ou [999 para parar: ]'))
    if n != 999:
        soma += n
        total+= 1
    else:
        soma - 999
print(f'Foram digitados no total de {total } numeros\nCom a soma o valor total e de {soma}')