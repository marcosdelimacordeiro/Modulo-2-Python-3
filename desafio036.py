# Escreva um programa para aprovar o emprestimo bancario para compra de uma casa. pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar. A prestacao mensal nao pode exceder 30% do salario ou entao o emprestimo sera negado

valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite o seu salario: '))
anos = int(input('Digite em quantos anos vai pagar: '))

mensal = anos * 12
valor_prestacao = valor_casa / mensal
total = valor_salario * (30/100)
print(f''' 
    Para pagar um casa de R$ {valor_casa} em {anos} anos, o valor da prestacao fica no valor de R$ {valor_prestacao:.2f} reais mensais.
      ''')
if valor_prestacao <= total:
    print(f'Apos analise o Emprestimo pode ser CONCEDIDO!')
else:
    print(f'Apos analise o seu Emprestimo NAO PODE SER CONCEDIDO!')