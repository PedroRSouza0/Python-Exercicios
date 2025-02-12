main_list = list()
copy_list = list()
people = 0
haviest = lightest = 0
while True:
    main_list.append(str(input('Digite um nome: ')))
    main_list.append(int(input('Digite o peso: ')))
    copy_list.append(main_list[:])
    main_list.clear()

    people += 1 # Conta o número de cadastrados

    op = str(input("Deseja continuar? [S/N]: "))
    if op not in 'Ss':
        break
    
for i in range(len(copy_list)): # Contagem de peso
        if j == 0:
            haviest = copy_list[i][j]
            lightest = copy_list[i][j]
        else:
            if copy_list[i][j] > haviest:
                haviest = copy_list[i][j]
            if copy_list[i][j] < lightest:
                lightest = copy_list[i][j]   
        i += 1

print(copy_list)    
print(f'O Total de pessoas cadastradas: {people}')

print(f'O Mais pesado foi {haviest}',end= '')
for i, v in enumerate(copy_list):
     if v == haviest:
        print(v,end= ' e ')

print(f'O Mais leve foi {lightest}',end= '')
for ii, vv in enumerate(copy_list):
    if vv == lightest:
        print(vv,end=' e ')    
