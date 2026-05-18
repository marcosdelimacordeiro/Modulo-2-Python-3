# refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:"""
# -EQUILATERO: todos os lados iguais
# -ISOSCELES: Dois lados iguais, um diferente
# -ESCALENO: todos os lados diferentes"""

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Podem Formar triangulo')
    if r1 != r2 != r3 != r1: # a diferenca sempre tem que testar todas a condicoes
        print(f'-ESCALENO: Todos os lados diferentes.')
    elif r1 == r2 == r3:
        print(f'-EQUILATERO: Todos os lados iguais.')
    else:
        print(f'-ISOSCELES: Dois lados iguais, um diferente.')
else:
    print(f'Não podem formar triangulo!')
