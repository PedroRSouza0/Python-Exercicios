'''038: Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem.
    - O Primeiro valor é maior.
    - O Segundo valor é maior.
    - Não existe valor maior, os dois são iguais.'''

n = int(input('Entre com o primeiro valor:\n'))
n2 = int(input('Entre com o segundo valor:\n'))

if n > n2:
    print('{} É maior que {}'.format(n, n2))
elif (n < n2):
    print('{} é maior que {}'.format(n2, n))
else:
    print('Não existe valor maior, os dois são iguais.')        

