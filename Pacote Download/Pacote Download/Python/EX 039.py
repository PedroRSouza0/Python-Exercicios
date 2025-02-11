'''039: Faça um programa que leia o ano de alistamento de uma pessoa e informe de acordo com a sua idade:
    - Se ele ainda vai se alistar.
    - Se é a hora de  se alistar.
    - Se já passou do tempo de se alistar.
Seu programa também deve mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date  
sexo = str(input('Informe seu sexo\nH - Masculino \ F - Feminino\n'))
nascimento = int         
idade = int   
atual = date.today().year


if (sexo.upper() == ('H')):
    ano = int(input('Digite o ano do seu alistamento:\n'))
    nascimento = (ano - 18)
    idade = (atual - nascimento)
    if idade == 18:
        print('Você está com {} anos, é hora de se alistar!'.format(idade))
    elif idade < 18:
        print('Você está com {} anos, você ainda vai se alistar daqui {} ano(s)!'.format(idade, ano - atual))
    elif idade > 18:
        print('Você está com {} anos, você deveria ter se alistado a {} ano(s) atrás!'.format(idade, atual - ano))           
elif sexo.upper() != ('F'):
    print('Digite uma resposta válida!')
else:
    print('Você é mulher.')     
       