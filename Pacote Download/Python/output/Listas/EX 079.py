listanum = list()

while True:
    num = int(input('Digite um número: '))

    if num in listanum:
        print('O Número digitado já existe, porfavor digite outro.')
    else:
        listanum.append(num)
        print('Número cadastrado com sucesso')

        while True:
            opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()

            if opcao == 'S':  # Da pra simplificar colocando not in, removendo assim o elif, otimizando o codigo
                break
            elif opcao == 'N':
                print('\nFinal\n')
                print(F'A Lista final foi: {sorted(listanum)}')
                exit() # Encerra o programa
            else:    
                print('Porfavor digite uma opção válida',end= ' ')
  