#041:

from datetime import date 

actual = date.today().year
born = int(input('Write the year that you born here:\n'))
age = actual - born

if age <= 9:
    print('You are {} years - MIRIM'.format(age))
elif age <= 14:
    print('You are {} years - INFANTIL'.format(age))   
elif age <= 19:
    print('You are {} years - JUNIOR'.format(age))
elif age == 20:
    print('You are {} years - SENIOR'.format(age))
else:
    print('Your are {} years - MASTER'.format(age))                  