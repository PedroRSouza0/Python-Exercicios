from time import sleep
i = 0 
opcao = ' '
print('P.A(zada) GAME')

primeiro = int(input('Digite o primeiro termo da P.A: '))
termos = int(input('Digite o número de termos desta P.A: '))
razao = int(input('Qual será a razão da P.A?: '))

while i < termos:
    print(F'{primeiro}', end = ' -> ')
    primeiro += razao
    i += 1
print('FIM')    

while True:
    opcao = str(input("Gostaria de ver mais alguns termos? [s/n]: ")).strip()
    
    if opcao not in ('N', 'n', 's', 'S'):
        print('Porfavor digite uma opcão válida')
    elif opcao not in ('N', 'n'):
        novo = int(input('Quantos termos?: '))
        termos += novo
        
        for i in range (i, termos):
            print(f'{primeiro}', end= ' -> ')
            primeiro += razao
            i += 1

    elif opcao in ('n', 'N'):
        break    

       
    print('PAUSE')
        
print("FIM")
print("Saindo...")
sleep(1)
print(f'Programa executado com {termos} progressões.')