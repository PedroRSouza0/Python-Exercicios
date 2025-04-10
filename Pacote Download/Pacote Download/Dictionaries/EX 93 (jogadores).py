gols = list()
data = dict()
total = 0

data['Nome'] = str(input('Digite o nome: '))
data['Partidas'] = int(input(f'Quantas partidas o {data["Nome"]} jogou?: '))
# Número de Partidas
for i in range(data['Partidas']):
    gols.append(int(input(f"Quantos gols na partida {i}: "))) # Lê os gols em cada partida
    total += gols[i]

data['Golls'] = gols #Insere a lista no dicionário
data['Total'] = total
print(data)
print()

for k, v in data.items():
    print(f'{k} = {v}')
print()    
print(f'O jogador {data['Nome']} jogou {data['Partidas']} partidas') # Arrumar indice
for i in range(len(gols)):
    print(f'Na partida {i} marcou: {gols[i]}')
print(f'Totalizando {total}')    
