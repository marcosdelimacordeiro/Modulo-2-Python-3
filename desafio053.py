# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos

frase = str(input('Digite uma frase para verificar se e palindromo: ')).strip().lower()

palavra = frase.split()  
# separa a frase em uma lista de palavras (remove os espacos)

junto = ''.join(palavra)  
# junta todas as palavras em uma unica string, sem espacos

inverso = ''  
# string vazia que vai armazenar a frase invertida

# laco for que percorre os indices da string 'junto' do ultimo ao primeiro
# a cada iteracao, o caractere correspondente e adicionado em 'inverso'
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

# compara a string original com a invertida
if junto == inverso:
    print('Palindromo!')
else:
    print('Nao e palindromo!')
