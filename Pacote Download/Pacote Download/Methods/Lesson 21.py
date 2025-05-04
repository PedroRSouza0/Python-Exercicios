# interactive help

# help()

# print(print.__doc__)

def teste(b):
    global a
    a = 8
    b += 1
    print(f'A dentro {a}')
    print(b)


a = 5
print(a)
teste(a)
