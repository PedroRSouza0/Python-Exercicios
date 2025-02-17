matriz = [[],[],[]]

for i in range(0,3):
    for j in range(0,3):
        num = int(input(f"Digite o valor para a posição {j}: "))
        matriz[i].append(num)
print('+-'*50)
for i in range(0, 3):
    for j in range(0,3):
        print(matriz[i][j],end= ' ')
    print()     
