extenso = 'Zero' , 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis'

while True:
    numero = int(input("Digite um numero de 0 a 6: "))
    if numero > 6 or numero < 0:
        print('Digite um valor válido')
    else:
        print(f'Você escolheu o número {extenso[numero]}')
        break    
    