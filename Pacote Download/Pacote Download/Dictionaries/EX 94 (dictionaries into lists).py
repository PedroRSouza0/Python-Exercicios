each = dict()
people = list()
option = ' '
tot = 0
average = 0
tot_woman = 0
while True:
    # Reading the data in dictionaries e put them into a list
    each['Name'] = str(input('Input your name: '))
    each['Gender'] = str(input('[F/M]: ')).upper()
    each['Age'] = int(input('Input your age: ')) 
    people.append(each.copy())

    tot += 1 #Plus one in the summary

    option = str(input('\nDo you want to continue? [Y/N]: ')).upper().strip()
    if option in 'Nn':
        break

print(people)

for i in range(len(people)):
    average += people[i]['Age']  # It calculates the average
print(f'The average was: {average/len(people)}')

# Now I am going to list all the womans
for i in range(len(people)):
    if people[i]['Gender'] == 'F':
        tot_woman += 1
print(f"The total of women were: {tot_woman}")    

# And to finishing it, There is a list with the total of people over the age
print('People over the age:\n')
for i in range(len(people)):
    if people[i]['Age'] >= 18:
        print(f'{people[i]['Name']}')
        