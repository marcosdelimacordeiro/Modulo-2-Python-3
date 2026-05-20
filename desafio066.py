# Crie um programa que leia numeros inteiros pelo teclado. o programa so vai para quando o usuario digitar o valor 999, que e a condicao de parada.No final, mostre quantos numeros foram digitados e qual foi a soma entre elas(desconsiderando o flag)
s=tot=0
while True:
    n = int(input('Digite um numero inteiro ou [999 para parar]: '))
    if n == 999:
        break
    s+=n
    tot += 1
print(f'Foram digitados total de {tot} numeros\nA soma total dos valores deu {s}.')