from random import randint
sortlist = []

for i in range(0,5):
    sortlist.append(randint(1, 50))
    
for ii in range(len(sortlist)): #Trava uma posição
    for j in range(len(sortlist)): #Vai comparar com as outras
        if sortlist[ii] < sortlist[j]:
            sortlist[j], sortlist[ii] = sortlist[ii], sortlist[j]
            
print(sortlist)
