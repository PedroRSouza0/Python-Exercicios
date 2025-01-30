lista = list()
for i in range(0,5):
    n = int(input('Digite um número: '))

    if i == 0 or n > lista[len(lista) - 1]: # Ultimo elemento da lista
        lista.append(n)
        print('Valor adicionado no final da lista...')
    else:
        # Fazer uma passagem por cada elemento do array
        ii = 0
        while ii < len(lista):
            if n <= lista[ii]: # Pega o elemento do array
                lista.insert(ii, n)
                print(f'Valor adicionado na posição {ii}')
                break
            ii += 1
print(lista)    
