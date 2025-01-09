import random
i = 0
tupla = tuple(random.randint(1, 100)for i in range(5))

print(f'Os numero sorteados foram: {tupla}')

for i in tupla:
    if tupla[i] > tupla[i+1]:
        print(f'O maior número foi {tupla[i]}')
      

    