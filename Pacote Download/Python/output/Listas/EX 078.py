lista = []
maior = 0
menor = 0

for i in range(0, 5):
    lista.append(int(input(f'Digite o {i} valor: ')))
    
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]    
  

print(f'\nLISTA COMPLETA: {lista}')

print(f'O Maior valor foi {maior} na posição ',end= '')
for v, p in enumerate(lista):
    if p == maior:
        print(f'{v}',end= ' e ')

print(f'\nO Menor valor digitado foi {menor} na posição ',end= '')
for v, p in enumerate(lista):
    if p == menor:
        print(f'{v}',end= ' e ')
        
