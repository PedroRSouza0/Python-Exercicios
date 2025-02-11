from random import randint

item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

escolha = int(input('Escolha\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura:\n'))


print("O jogdaor escolheu {}".format(item[escolha]))
print('O computador escolheu {}'.format(item[computador]))

if computador == 0:
    if escolha == 0:
        print('Empate')
    elif escolha == 1:
        print('Jogador Vence')
    else:
        print('Computador Vence')    
if computador == 1:
    if escolha == 0:
        print('Computador vence') 
    elif escolha == 1:
        print('Empate')       
    else:
        print('Jogador vence')
if computador == 2:
    if escolha == 0:
        print('Jogador vence')
    elif escolha == 1:
        print('Computador vence')
    else:
        print('empate')                    

        '''CONSIDERAR JOGADA INVALIDA'''
        