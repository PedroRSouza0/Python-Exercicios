#def showline():
 #   print('-' * 30)

#showline()
#print('I am tired, but I am going to study even')
#showline()
'''
Function without parameters
'''

def showline(text):
    print('=' * 45)
    print(text)
    print('=' * 45)


#showline('That"s alright')

def soma(a, b):
    return a + b # Function with return
'''print(soma(1,9))''' # Fuction with return gets the value and let it save, if you want to put out it you need to use another method

def somalocal(a, b):
    s = a + b
    print(s) # Fuction without return

# somalocal(1,19)    

def contador(*x): # Undefined Parameters function (This allows you put how many arguments you want into the function, at the end python saves them into a tuple, so for you use them you'll need to use as a tuple)
    for i in x:
        print(i,end= ' ')

contador(2,3,51,2,5)       


lista = [2,5,6] # Lists as arguments
def double(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1 
    return list

print(double(lista))

