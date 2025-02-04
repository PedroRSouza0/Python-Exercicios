expression = list()
input = str(input('Write some algebric expression who use parens: '))

for parens in input: # Para cada valor em input
    if parens == '(':
        expression.append('(') # Se parens == aberto add
    elif parens == ')':
        if len(expression) > 0: # Se parens == fechado só add se tiver parens aberto e elimine o ultimo
            expression.pop()
        else:
            expression.append(')') # Se parens == fechado sem ter nenhum aberto, erro no programa
            break 
if len(expression) == 0:
    print('Correct')
else:
    print('Incorrect')               
