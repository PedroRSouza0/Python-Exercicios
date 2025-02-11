titulo = 'Bem Vindo'

produto = ()

while True:
    print(titulo.center(30, '='))

    print("Escolha uma das opções abaixo\n")
    print("1 - Cadastrar Produto")
    print("2 - Vizualizar Estoque")
    print('3 - Sair')

    escolha = int(input(': '))

    if escolha == 1:
        while True:
            #Testar com variavel de loop
            for i in range():
                produto[] = str(input('Digite o nome do seu produto:\n'))
                produto[] = str(input('Digite a quantidade do seu produto:\n'))
            
            iteração = str(input('Deseja cadastrar mais produtos? [Y/N]\n')).strip().upper()
            if iteração == 'N':
                break

    if escolha == 2:
        print(produto)

    if escolha == 3:
        break         
