from time import sleep

def Counter(start, end, step):
    # First Count
    print('\nFirst one')
    for i in range(1,10+1):
        print(i, end= ' ')
        sleep(0.5)

    # Second Count
    print("\nSecond")
    for i in range(10, -1, 2):
        print(i, end= ' ')   
        sleep(0.5)    

    # Personal Count
    while True:
        try: 
            start = int(input("Start: "))
            end = int(input('End: '))
            step_input = input('Step: ').strip()

            # Tratamento, se vazio == 1
            if step_input == '' or step_input == 0:
                step = 1
            else:
                step = abs(int(step_input)) # Se negativo vira positivo
        
                if step < 0:
                    step = abs(step)
            break
        except ValueError:
            print('Entrada invalida')

        # Verificando a contagem
        if start < end:
            # Contagem crescente
            for i in range(start,end+1,step):
                print(i, end=' ')
                sleep(0.5)

        # Contagem decrescente
        elif start > end:
            for i in range(start,end,-step):
                print(i,end= ' ')
                sleep(0.5)
        else:
            print('Start e end são iguais')
    
Counter(1,32,1)