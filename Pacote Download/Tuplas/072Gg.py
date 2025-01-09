extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete')

while True:
    numero = int(input("Digite um número de 0 a 7: "))
    if not (0 <= numero <= 7): #Negação
        print('Digite um valor válido.', end= ', ')
    else:
        print(f'Você escolheu o número {extenso[numero]}')    

        print("Você deseja continuar? [S/N]", end= ': ')
        opcao = str(input()).strip().upper()

        if opcao != 'S':
            break
        