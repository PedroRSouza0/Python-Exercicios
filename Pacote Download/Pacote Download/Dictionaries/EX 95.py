jogadores = list()

while True:
    data = dict()  # Dicionário de jogadores (cada jogador é um dicionário)
    gols = list()

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
    print(f"- {i} | Nome: {jogador['Nome']} | Partidas: {jogador['Partidas']} | Gols: {jogador['Gols']} | Total: {jogador['Total']} ")

# Loop para consultar jogador
while True:
    dados = int(input('\nDeseja observar dados de qual jogador? [-1 para sair]: '))
    
    if dados == -1:
        break  # Encerra o loop se o usuário digitar -1
    
    if dados >= len(jogadores) or dados < 0:
        print(f'ERRO! Não existe jogador com o código {dados}.')  # Verifica se o código digitado é válido
    else:
        jogador = jogadores[dados]
        print(f"\n-- LEVANTAMENTO DO JOGADOR {jogador['Nome']}:")
        print(f"   Número de partidas: {jogador['Partidas']}")
        for i, g in enumerate(jogador['Gols']):
            print(f"   No jogo {i + 1} fez {g} gols.")
        
        print("\nPrograma finalizado após consulta.")
        break  # Encerra o programa após mostrar os dados do jogador
