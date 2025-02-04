numeros = list()
total5 = 0
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    op= str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if op != 'S'and op != 'N':
        print('Digite uma opção válida',end= ' ')
        op = str(input("Deseja continuar? [S/N]: ")).upper().strip()
        if op == 'N':
            break
    if op == 'N':
        break
for i, ii in enumerate(numeros):
    if ii == 5: 
        total5 += 1       
print()
print(f'O Total de valores digitados foi {len(numeros)}')
numeros.sort(reverse= True)
print(f'A Lista ordenada de maneira decrescente: {numeros}')
if 5 in numeros:
    print(f'O Cinco apareceu na lista, {total5} vezes.')
else:
    print('O Cinco não apareceu na lista')    
