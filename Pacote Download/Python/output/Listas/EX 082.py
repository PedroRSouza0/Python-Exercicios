#Este exercicio consiste em ler dinamicamente valores e armazena-los em uma lista e no final adicionar alguns valores para outras listas de acordo com suas devidas condições

lista = []
listapar = list()
listaimp = list()
i = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    
    if lista[i] % 2 == 0:
        listapar.append(lista[i])
    else:
        listaimp.append(lista[i])
    i+=1

    op = str(input('Deseja continuar? [S/N]: '))
    if op not in 'Ss':
        break

print(lista)
print('Lista somente com os pares {}'.format(listapar))
print(f'Lista somente com os impares {listaimp}')

# Ou pode se fazer deste jeito
# for i, v in enumerate(lista):
    # if v % 2 == 0:
        # listapar.append(v)
    #else:
    # 
    # a parada é que ele varre todos os elementos da lista, e depois adiciona (isso com a lista feita), no exemplo que eu fiz ele analisa já no momento em que usuario insere, analisando e armazenando cada numero individualmente
    #     