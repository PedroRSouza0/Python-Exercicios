people = dict()

# for i in range(0,3):
  #  people[i] = str(input("Digite o valor do indice e da variavel: "))
# print(people)     
'''
The loop just reads only the values, the keys are standard : {}'0' : value , '1' : value} and so on
'''

personS = {'Name': 'Pedro', 'Gender':'M', 'Age' : 19 }
# for k, v in personS.items():
  #  print(f'{k} / {v}') for standard python prints the keys if you do not especify

#del personS['Name']
#print(personS)

#personS['Height'] = 1.75
#print(personS)

for i in range(0,3):
    people['nombre'] = str(input('Digite o seu nome: '))
    people['idade'] = int(input('Digite a idade: '))
    people.copy()
print(people.items())    

'''continue it'''