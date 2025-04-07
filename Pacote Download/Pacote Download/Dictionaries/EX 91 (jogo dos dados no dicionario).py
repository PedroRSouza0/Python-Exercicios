from random import randint
from time import sleep

# I have declared a dictionary
dic = dict() 
# Input of the values using and creating into the for the keys as well
for i in range(1,4+1):
    dic[i] = randint(1,6)
# Output    
for k, v in dic.items():
    print("Player {} got {}".format(k,v))
    sleep(1)

print()
print("Player's Ranking:")
print()
#Ordering the dictionary
for v in dic.values():
    for value in dic.values(): #Error, but this is a selection sort
        if v > value:
            value, v = v, value
print(dic)            
