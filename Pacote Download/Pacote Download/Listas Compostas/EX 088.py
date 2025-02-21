import random
import time

jogos = 0
lista_copia = list()
lista_current = list()

print('-'*30)
print('MEGA SENA'.center(30))
print('-'*30)
print()

jogos = int(input('Quantos jogos serão jogados?: '))
print("SORTEANDO...")
total = 1

while total <= jogos: #Bloco para adicionar x jogos
    cont = 0 # Para resetar a cada iteração    
    while True: #Bloco para adicionar 6 numeros
        numeros = random.randint(1, 60)
        if numeros not in lista_copia:
            lista_copia.append(numeros)
            cont += 1
        if cont >= 6:
            break

    lista_copia.sort()
    lista_current.append(lista_copia[:])
    lista_copia.clear()
    total += 1

for i, v in enumerate(lista_current):
    time.sleep(0.5)
    print(f'Jogo {i+1} - {v}')
