main_list = list()
copy_list = list()
people = 0
while True:
    main_list.append(str(input('Digite um nome: ')))
    main_list.append(int(input('Digite o peso: ')))
    copy_list.append(main_list[:])
    main_list.clear()

    people += 1 # Conta o número de cadastrados
    for i in range(len(copy_list)): # Contagem de peso 
        if copy_list[]

    op = str(input("Deseja continuar? [S/N]: "))
    if op not in 'Ss':
        break

print(copy_list)    
print(f'O Total de pessoas cadastradas: {people}')
