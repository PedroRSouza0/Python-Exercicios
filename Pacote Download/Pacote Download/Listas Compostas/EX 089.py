from time import sleep
first_list = list()
copy_list = []
media_list = list()
while True:
    first_list.append(str(input('Digite o seu nome: ')))  # 0
    first_list.append(float(input('Digite sua primeira nota: '))) # 1
    first_list.append(float(input('Digite a segunda nota: '))) # 2

    media = (first_list[1] + first_list[2])/2
    media_list.append(media)

    copy_list.append(first_list[:])
    first_list.clear()

    
    opcao = str(input('\nDeseja continuar?[S/N]: ')).upper().strip()
    if opcao != 'S':
        break

print('-'*50)
print("Boletim Final".center(50))
print('-'*50)
for i in range(len(copy_list)):
    print(f'N°: {i} - Nome: {copy_list[i][0]} - Média: {media_list[i]}')
    
opcao_dois = int(input('\nDeseja ver as notas de qual aluno? [DIGITE O NÚMERO/999 p sair]: '))
if opcao_dois == 999:
    print('Saindo')
    for i in range(0,3):
        print('.',end= '')
        sleep(0.5)
else:
    for i in range(len(copy_list)):
        if opcao_dois == i:
            print(f'{copy_list[i][0]} - NOTA 1: {copy_list[i][1]} - NOTA 2: {copy_list[i][2]}')
# FAZER TRATAMENTO DE ERRO
