from time import sleep

def maior(*num):
    print('-='*20)
    Maior = num[0] # Primeiro numero
    total = len(num)
    
    print(f'The chosen numbers were {total}: ',end= '')
    for i in num:
        if i > Maior:
            Maior = i
        print(i, end= ' ', flush=True)
        sleep(0.5)
    
    print(f'\nThe bigger one was: {Maior}')    
    print('-='*20)


maior(6)
maior(1,5,2,400,123)
maior(5,5,1)
