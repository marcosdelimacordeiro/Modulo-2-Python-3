# Refaca o Desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizar um laco for

n = int(input('Digite um valor de tabuada que desejar: '))

for c in range(0,11):
    print(f'{n} X {c:2} = {n*c}')