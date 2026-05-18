# Escreva um programa em python que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao: 1 para binario, 2 para octal e 3 para hexadecimal
# nao preciso importa modulo porque as funcoes que foram usadas sao builtin
numero = int(input('Digite qualquer numero inteiro: '))
conversao = int(input('''
Para qual base deseja converter digite:
1 - Binario
2 - Octal
3 - Hexadecimal
            
'''))
if conversao == 1:
    binario = bin(numero)
    print(f'O numero {numero} convertido para binario fica o valor {binario[2:]}')
elif conversao == 2:
    octal = oct(numero)
    print(f'O numero {numero} convertido para octal e o valor {octal[2:]}')# foi usado o fatiamento pois os dois primeiros ele mostra o base que esta convertido.
elif conversao == 3:
    hexadecimal = hex(numero)
    print(f'O numero {numero} convertido para Hexadecimal e o valor {hexadecimal[2:]}')
else:
    print(f'Opcao invalida!')