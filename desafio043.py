# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu indice de massa corporal(IMC) e mostre seus status, de acordo com a tabela abaixo: """
# -IMC abaixo de 18.5: abaixo do peso
# - Entre 25 ate 30 :sobrepeso
# - 30 ate 40 : obesidade
# - Acima de 40: obesidade morbida
# ""
from math import pow
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso  / (pow(altura , 2))
print(f'Seu peso {peso}KG e sua altura de {altura}M, seu IMC: seu IMC e de {imc:.2f}')
if imc < 18.5:
    print(f'- IMC abaixo de 18.5: Abaixo de peso.')
elif 18.5 <= imc < 25:
    print(f'- Entre 18,5 e 25: PESO IDEAL.')
elif 25 <= imc < 30:
    print(f'-25 ate 30: SobrePeso')
elif 30 <= imc <40:
    print(f'-30 ate 40: Obesidade')
else:
    print(f'-Acima de 40: Obesidade Morbida.')