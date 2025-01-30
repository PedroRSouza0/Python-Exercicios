lista = []
for i in range(0,5):
    n = int(input('Digite um número: '))

    if i == 0 or n > lista[len(lista) -1 ]:
        lista.append(n)
        print('Valor adicionado no final.')

    # Varrer o resto do vetor num por num
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')    
                break
            pos += 1
print('FINAL:')            
print(lista)        
