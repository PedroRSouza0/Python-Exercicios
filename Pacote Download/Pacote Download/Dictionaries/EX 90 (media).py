dic = dict()

dic['Name'] = str(input("Write your name: "))
dic['Average'] = float(input('Put your average: '))

if dic['Average'] >= 7: # See if the student is aproved ou not
    dic['Situation'] = 'Aproved'
else:
    dic['Situation'] = 'Reproved'

# Print the structure of the dictionary , showing all the items
for k, v in dic.items():
    print(f'{k} = {v}')
