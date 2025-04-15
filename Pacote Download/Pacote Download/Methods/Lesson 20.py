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
    return a + b

# print(soma(1,9))

def somalocal(a, b):
    s = a + b
    print(s)

somalocal(1,19)    
