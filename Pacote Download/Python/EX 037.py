'''037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
        1 - para Binario
        2 - para Octal
        3 - para Hexadecimal'''

# Switch case?

num = int(input('Digite um valor inteiro para a conversão:\n'))
opcao = int(input('Escolha a base em que iremos converter o seu número\n1 - Binario\n2 - Octal\n3 - Hexa\n'))

if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])    
elif (opcao == 3):
    print(hex(num)[2:])
else:
    print('DIGITE UMA OPCAO VALIDA')        

          