first_list = list()
copy_list = []
media_list = list()
while True:
    first_list.append(str(input('Digite o seu nome: ')))
    first_list.append(float(input('Digite sua primeira nota: ')))
    first_list.append(float(input('Digite a segunda nota: ')))

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

