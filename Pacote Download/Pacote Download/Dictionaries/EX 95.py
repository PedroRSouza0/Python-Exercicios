jogadores = list()

while True:
    data = dict()  # Dicionário de jogadores (cada jogador é um dicionário)
    gols = list() # Poderia tambem ter apenas limpado cada conjunto

    data['Nome'] = str(input('Digite o nome: '))
    data['Partidas'] = int(input(f'Quantas partidas o {data["Nome"]} jogou?: '))

    # Número de Partidas
    for i in range(data['Partidas']):
        gols.append(int(input(f"Quantos gols na partida {i + 1}: ")))  # Lê os gols em cada partida

    data['Gols'] = gols[:]
    data['Total'] = sum(gols)

    jogadores.append(data.copy())

    while True:
        option = str(input('\nDo you want to continue? [Y/N]: ')).upper()
        if option in 'YN':
            break
        print('ERROR. Choose a valid option')
    if option == 'N':
        break

# Exibe todos os jogadores cadastrados
print('-=' * 50)
for i, jogador in enumerate(jogadores):
    print(f"- {i:>5}",end=' ')
    for v in jogador.values():
        print(f'{str(v):<15}',end=' ') #Forçar tudo a ser string para conseguir formatar 
    print()

# Loop para consultar jogador
while True:
    dados = int(input('\nDeseja observar dados de qual jogador? [-1 para sair]: '))
    
    if dados == -1:
        break  # Encerra o loop se o usuário digitar -1
    
    if dados >= len(jogadores) or dados < 0:
        print(f'ERRO! Não existe jogador com o código {dados}.')  # Verifica se o código digitado é válido

    else:
        jogador = jogadores[dados] # Poderia ser feito com loop na lista, acessando as keys com i 
        print(f"\n-- LEVANTAMENTO DO JOGADOR {jogador['Nome']}:")
        print(f"   Número de partidas: {jogador['Partidas']}")
        for i, g in enumerate(jogador['Gols']):
            print(f"   No jogo {i + 1} fez {g} gols.")

        while True:
            outro = str(input('Deseja ver outro jogador? [S/N]')).upper()
            if outro in 'SN':
                break
            print('Escolha uma opção valida')

        if outro == 'N':
            print('Fim do programa')
            break  
            
        