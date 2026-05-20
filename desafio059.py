#crie um programa que leia dois valores e mostres um menu na tela
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa
n1 = float(input('Digite primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 1
while opcao != 5:
    opcao = int(input(''' 
    Escolha sua opcao: 
    [1] - Somar 
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Numeros
    [5] - Sair
    '''))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        multiplicacao = n1 * n2
        print(f'O resultado da multiplicacao de {n1}X{n2} é {multiplicacao}')
    elif opcao == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior valor e {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior valor e {n2}')
        else:
            print(f'Os valores {n1} e {n2} sao iguais')
    elif opcao == 4:
        n1 = float(input('Digite o novo valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao not in (1,2,3,4):
        print(f'Opcao invalida! Tente novamente')
    else:
        print(f'Finalizando...')
print(f'O programa foi finalizado!')