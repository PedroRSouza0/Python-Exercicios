tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corithians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'O G5 Foi: {tabela[:5]}\n')

print('Os rebaixados foram: {}\n'.format(tabela[-4:]))

print(f'Os times em ordem alfabética {sorted(tabela)}')

print(f'O Vasco ficou na {tabela.index('Vasco') + 1} posição')
