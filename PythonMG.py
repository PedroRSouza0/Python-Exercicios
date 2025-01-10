from time import sleep
i = 0
option = ' '
print('P.A(zada) GAME')

first_term = int(input('Enter the first term of the A.P: '))
num_terms = int(input('Enter the number of terms in this A.P: '))
difference = int(input('What will be the common difference of the A.P?: '))

while i < num_terms:
    print(f'{first_term}', end=' -> ')
    first_term += difference
    i += 1
print('END')

while True:
    option = str(input("Would you like to see more terms? [y/n]: ")).strip()
    
    if option not in ('N', 'n', 'y', 'Y'):
        print('Please enter a valid option.')
    elif option not in ('N', 'n'):
        new_terms = int(input('How many terms?: '))
        num_terms += new_terms
        
        for i in range(i, num_terms):
            print(f'{first_term}', end=' -> ')
            first_term += difference
            i += 1

    elif option in ('n', 'N'):
        break    

    print('PAUSE')
        
print("END")
print("Exiting...")
sleep(1)
print(f'The program executed with {num_terms} progressions.')
