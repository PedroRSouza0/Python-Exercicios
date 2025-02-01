lista = []
totalnum = 0
totalcinco = 0
i = 0

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    totalnum += 1

    # Tratamento de erro
    op = str(input('Deseja continuar? [S/N]:')).upper().strip()
    while op not in ('S','N'):
        print('Digite uma opção válida.')
        op = str(input('Deseja continuar? [S/N]:')).upper().strip()
    if op == 'N':
        break

for i in range(len(lista)):
    if lista[i] == 5:
        totalcinco += 1
        
print()
print('Total de número digitados: {}'.format(len(lista)))

lista.sort(reverse= True)
print(f'Lista Ordenada ao contrário: {lista}')

if 5 in lista:
    print('O número 5 apareceu {} vezes'.format(totalcinco))
else:
    print('O número 5 não apareceu na lista.')
