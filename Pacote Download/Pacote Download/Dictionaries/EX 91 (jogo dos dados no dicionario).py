from random import randint
from time import sleep
from operator import itemgetter
# I have declared a dictionary
dic = dict() 

# Input of the values using and creating into the for the keys as well
for i in range(1,4+1):
    dic[i] = randint(1,6)

  
# Output    
for k, v in dic.items():
    print("Player {} got {}".format(k,v))
    sleep(1)


print("\nPlayer's Ranking:\n")

#Ordering the dictionary
ranking = dict()
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True) #This will return a list , so until now ranking need to be used as a list
for k, v in enumerate(ranking):
    print(f'{k+1}° Player {v[0]} got {v[1]}')    #here it is different, because enumerate is a loop so, k will be a index from 0 to x, v is a value, but here v is the tuple because we are into a list, each v will be like this: (key, value). Because of that it's need to use v[index]  
    sleep(1)