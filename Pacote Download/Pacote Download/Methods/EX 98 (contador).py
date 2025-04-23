from time import sleep

def Counter():
    # First Count
    print('\nFirst one')
    for i in range(1,10+1):
        print(i, end= ' ')
        sleep(0.5)

    # Second Count
    print("\nSecond")
    for i in range(10, 0, -2):
        print(i, end= ' ')   
        sleep(0.5)    

    print()

    # Personal Count
    while True:
        print('~'*20)
        start = int(input('The First one: '))
        end = int(input("The Last one: "))
        step = int(input('Step: '))

        if step < 0:
            step = abs(step)
            print(step)
            break
        elif step == 0:
            step = 1
        
        #Contagem crescente
        if start <= end:
            for i in range(start, end +1, step):
                print(i, end= ' ')
                sleep(0.5)
            break
        # Contagem decrescente
        if start >= end:
            for i in range(start, end -1, -step):
                print(i,end= ' ')
                sleep(0.5)
            break
        '''if start == end:
            print('Os valores são iguais')
            break''' # Corrigir este bloco



Counter()
