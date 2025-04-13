each = dict()
people = list()
option = ' '
tot = 0
average = 0
tot_woman = 0
while True:
    # Reading the data in dictionaries e put them into a list
    each['Name'] = str(input('Input your name: '))
    while True:
        each['Gender'] = str(input('[F/M]: ')).upper()
        if each['Gender'] in 'MF': #Error validation
            break
        print("ERROR. Please, write something allowed")

    each['Age'] = int(input('Input your age: ')) 
    people.append(each.copy())

    tot += 1 #Plus one in the summary
    while True:
        option = str(input('\nDo you want to continue? [Y/N]: ')).upper().strip()
        if option in 'YN':
            break
        print('ERROR, Just write Y/N')
    if option == 'N':
        break

print(people)
print(f'O total of people were: {tot}')

for i in range(len(people)): # I could calculate the average while I am getting the values, and in the end I just divide it for the len()
    average += people[i]['Age']
average/len(people)  # It calculates the average
print(f'The average was: {average}')

# Now I am going to list all the womans
for i in range(len(people)):
    if people[i]['Gender'] == 'F':
        tot_woman += 1
print(f"The total of women were: {tot_woman}")    

# And to finishing it, There is a list with the total of people over the age
print('People over the age:\n')
for i in range(len(people)):
    if people[i]['Age'] >= average:
        print(f'{people[i]['Name']}')
        