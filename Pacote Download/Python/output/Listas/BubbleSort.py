lista = list()
for i in range(0,5):
    n = int(input(f"Digite o {i} valor: "))
    lista.append(n)

    for i in range(len(lista)): # Isola cada elemento da lista
        for j in range(len(lista) - 1): # Trata o elemento j individualmente, comparando com todos até acabar
            if lista[j + 1] < lista[j]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]
  
print()
print('Lista Final:')
print('#'*30)
print(f'{lista}')            
        