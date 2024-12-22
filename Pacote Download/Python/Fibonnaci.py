t3 = t1 = 0
t2 = 1
i = 3
opcao = ' '

n = int(input('Quantos termos da sequencia de Fibonnacci voce gostaria de ver? '))
print(f'{t1} -> {t2}', end = ' -> ')

while(i <= n):
    t3 = t1 + t2
    print(f' {t3}' , end = ' -> ')
    t1 = t2
    t2 = t3
    i += 1

while opcao != 'N':
    opcao = str(input('Gostaria de ver mais alguns termos? [s/n]\n')).upper().strip()
    
    if opcao not in ('S','N'):
        print('Digite uma opcao válida')
    elif opcao == 'S':
        novo = int(input('Quantos termos? '))
        n += novo

    while(i <= n):
        t3 = t1 + t2
        print(f' {t3}' , end = ' -> ')
        t1 = t2
        t2 = t3
        i += 1  

print('FIM')    
