# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final, de acordeo com a media atingida
# - media abaixo de 5.0: REPROVADO
# - media entre 5.0 e 6.9: recuperacao
# - media 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >=7:
    print(f'Sua media foi: {media}, APROVADO! ')
elif 7> media >= 5: # Jeito python aceita como na matematica
    print(f'Sua media foi: {media}, situacao: RECUPERAÇÃO!')
else:
    print(f'Sua media foi: {media} situacao: REPROVADO!')