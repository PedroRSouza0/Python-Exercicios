expression = list()
keys = closekeys = 0
input = str(input('Digite uma expressão qualquer que use parênteses: '))

for parens in input:
    if parens == '(':
        expression.append('(')
    elif parens == ')':
        if len(expression) > 0:
            expression.pop()
        else:
            expression.append(')')
            break 
if len(expression) == 0:
    print('Correto')
else:
    print('Incorreto')               


    