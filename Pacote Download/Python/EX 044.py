produto = float(input('Digite o valor do seu produto: '))

print('[1] - á vista dinheiro/cheque.\n[2] - á vista no cartão.\n[3] - Em até 2x no cartão.\n[4] - 3x ou mais no cartão.')
escolha = int(input(': '))



if escolha == 1:
    print('Voce ganhou um desconto de 10%, seu produto passa a custar {:.2f}.'.format(produto - (produto*10)/100))
elif escolha == 2:
    print('Voce ganhou um desconto de 5%, o seu produto passa a custar {:.2f}.'.format(produto - (produto*5)/100))
elif escolha == 3:
    print('Preço parcelado {:.2f}'.format(produto/2))
elif escolha == 4:
    parcelas = int(input('Em quantas parcelas:\n'))
    precinho = produto / parcelas
    print('Valor com juros da parcela : {:.2f}'.format(precinho + produto*20/100))
else:
    print('Digite uma opção válida')
          
        # Fazer em C e fazer a evolução de nao deixar passar do limite de parcelas ou menor que o limite