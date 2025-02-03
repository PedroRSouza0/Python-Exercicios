expression = list()
keys = closekeys = 0
input = str(input('Digite uma expressão qualquer que use parênteses: '))
expression.append(input)

for i, v in enumerate(expression):
    if v == '(':
        keys += 1
    elif v == ')':
        closekeys += 1    

if '(' not in expression and ')' not in expression:
    print('Your expression is not avaliable')
elif closekeys != keys:
    print('Sua expressão não é válida, algum parentese não foi fechado corretamente')
else:
    print("Great job! The expression of yours is avaliable")    
