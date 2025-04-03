dic = dict()

dic['Name'] = str(input("Write your name: "))
dic['Average'] = float(input('Put your average: '))

if dic['Average'] >= 7:
    dic['Situation'] = 'Aproved'
else:
    dic['Situation'] = 'Reproved'

for k, v in dic.items():
    print(f'{k} = {v}')
