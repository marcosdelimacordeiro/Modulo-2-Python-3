# crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado(nimero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregue
# obs: considere que o caixa possui cedulas de R$ 50, R$ 20, R$ 10 e R$ 1
print('='*20)
print(f'{"Banco Central":^20}')
print('='*20)
valor = int(input('Digite um valor para sacar: R$ '))
total = valor
ced = 50 
tot_ced = 0 

while True:
    if total >= ced:
        total -= ced
        tot_ced +=1
    else:
        if tot_ced > 0:
            print(f'Total de cedula {tot_ced} do R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0 
        if total == 0:
            break
print('='*20)
print(f'Obrigado por sua Banco Central! Volte sempre!.')