import time
from random import randint
numbers = list()

def sorteia():
    print('Random numbers: ',end='')
    for i in range(0,5):
        numbers.append(randint(0,10))
        print(numbers[i],end= ' ', flush=True)
        time.sleep(0.5)
    print('DONE!')


def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Soma do pares {lista}: {soma}')


sorteia()
somapar(numbers)
