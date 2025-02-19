main_matrix = [[],[],[]]
somapar = somatres = 0
#Leitura dos dados
for i in range(0,3):
    for j in range(0,3):
        num = int(input(f'Digite um número para a posição [{i}][{j}]: '))
        if num % 2 == 0: # Verifica se o número é par e adiciona na soma
            somapar += num
        if j == 2: # Soma os números da terceira coluna
            somatres += num    
        main_matrix[i].append(num)

print('+='*50)
maior = main_matrix[1][0]

# Saída dos dados
for i in range(len(main_matrix)): # Estudar o que o -1 tava causando
    for j in range(len(main_matrix)):
        print(f'[{main_matrix[i][j]:^5}]',end= ' ')
    print()

print(f'A soma de todos os números pares da matriz resultou em: {somapar}')
print(f'A soma de todos os números da terceira coluna foi: {somatres}')
# Verificando o maior valor da segunda linha
for n in main_matrix[1]:
    if n > maior:
        maior = n
print(f'O maior valor da segunda linha foi: {maior}')
