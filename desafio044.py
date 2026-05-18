# Elabore um programa que calcule o valor a ser pago por produto, considerado o seu preco normal e condicao de pagamento """
# - á vista dinheiro/cheque: 10% de desconto 
# - á vista no cartao: 5% de desconto
# - em ate 2x no cartao: preco normal
# - 3x ou mais no cartao: 20% de juros"""

preco = float(input('Digite o preco do produto: '))
print("""
[1] - À vista dinheiro/cheque: 10% de desconto
[2] - À vista no cartao: 5% de desconto
[3] - Em até 2x no cartao: preco normal
[4] - 3x ou mais no cartao: 20% de juros
[5] - sair
""")
forma_pagamento = int(input('Qual forma de pagamento: '))
if forma_pagamento == 1:
    desconto = preco - (preco * (10/100))
    print(f'-À vista dinheiro/cheque: 10% de desconto, o valor do produto fica R$ {desconto:.2f} reais.')
elif forma_pagamento == 2:
    desconto = preco - (preco * (5/100))
    print(f'- À vista no cartao: 5% de desconto, o preco do seu produto fica valor de R$ {desconto:.2f} reais.')
elif forma_pagamento == 3:
    valor = preco / 2 
    print(f'- Em até 2x no cartao: preco normal, seu produto fica em 2X de R$ {valor:.2f} reais.')
elif forma_pagamento == 4:
    preco_juros = preco + (preco * (20/100))
    print(f'O valor com juros de 20% fica total de R$ {preco_juros:.2f} reais.')
    prestacao = int(input('O valor pode ser parcela de 3X ou ate 10X, digite o tanto de parcela que voce quer: '))
    valor = preco_juros / prestacao
    print(f'O valor total fica em R$ {preco_juros:.2f} reais\nSera pago em {prestacao} vezes de R$ {valor:.2f} reias.')
else:
    print(f'Obrigado, volte sempre!!')