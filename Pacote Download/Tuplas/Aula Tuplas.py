aniversarios= (1, 9, 17, 24, 28, 13) #Tupla Inicializada

print(type(aniversarios)) # Class Tuple

print(aniversarios[:2+1]) # Fatiamento

print(len(aniversarios)) # Comprimento

for i in range(0 , 5+1): # Array C style hehe
    print(aniversarios[i])

for i in aniversarios: # Python style. Using yourself tuple on the range
    print(i)
print('=-'*40)
print('\nAULA PRÁTICA\n')

print(f'{aniversarios[-2]}\n')

for i in range(0, len(aniversarios)):
    print(aniversarios[i])

print('\n')

# To show the element and the position of tuple:
for i, data in enumerate(aniversarios):
    print(f'Dia {data} na posição {i}')

# Ordering a Tuple:
print('\n')
print(sorted(aniversarios))   
print('\n')

# Using two tuples:
a = 3, 4, 5, 2
b = 4, 4, 2
c = b + a
print(c)
print(f'\n{c.count(4)}') # This function show us how many times the element chose show
print(f'{c.index(5)}\n') # This show us who is the position that our element will show, if you chose an element who has more same it, the function will show the first one

# or you can do this way
print(f'{c.index(2,4)}')
