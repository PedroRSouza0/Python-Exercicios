from time import sleep


def Contador(start, end, step):

    """  Faz uma contagem e mostra na tela
    Parameter start -> inicio
    Parameter end -> fim
    Parameter step -> passo
    return -> no return
    
    """    

    if step < 0:
        step = abs(step)
    if step == 0:
        step = 1

    print(f'Contagem de {start} a {end} de {step} em {step}')
    print()

    if start < end: # Contagem Crescente
        i = start
        while i <= end:
            print(i,end= ' ',flush=True)
            sleep(0.5)
            i += step
        print('FIM')
    elif start > end: # Contagem decrescente
        i = start
        while i >= end:
            print(i, end= ' ',flush=True)
            sleep(0.5)
            i -= step
        print('FIM')
    else:
        print('Os números são iguais')


print('Conta personalizada')
first = int(input('Inicio: '))
last_one = int(input('Fim: '))
passo = int(input('Passo: '))
print('-=' * 20)
Contador(first, last_one, passo)
