from random import randint
sortlist = []
for i in range(0,5):
    sortlist.append(randint(1, 50))
    

    #bubble sort
for ii in range(len(sortlist)): #Controla o número de repetições necessarias
    for j in range(len(sortlist) - 1): #Compara com a mesma variavel uma casa a frente
        if sortlist[j] < sortlist[j + 1]:
            sortlist[j + 1], sortlist[j] = sortlist[j], sortlist[j + 1]   
print(sortlist)

    #selection sort
'''for ii in range(len(sortlist)): #Trava uma posição
    for j in range(len(sortlist) : #Vai comparar com a variavel travada
        if sortlist[ii] < sortlist[j]:
            sortlist[j], sortlist[ii] = sortlist[ii], sortlist[j]'''