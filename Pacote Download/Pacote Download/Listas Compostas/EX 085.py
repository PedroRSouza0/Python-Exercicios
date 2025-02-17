main_list = [[],[]]

for i in range(0,7):
    num = int(input(f'Digite o valor {i}°: '))
    if num % 2 == 0:
        main_list[0].append(num)
    else:
        main_list[1].append(num)

for i in range(len(main_list[0]) - 1):
    for j in range(len(main_list[0])- 1 - i):
        if main_list[0][j] > main_list[0][j + 1]:
            main_list[0][j + 1], main_list[0][j] = main_list[0][j], main_list[0][j+ 1]

for i in range(len(main_list[1]) - 1):
    for j in range(len(main_list[1])- 1 - i):
        if main_list[1][j] > main_list[1][j + 1]:
            main_list[1][j + 1], main_list[1][j] = main_list[1][j], main_list[1][j+ 1]
           
            
print(main_list)
