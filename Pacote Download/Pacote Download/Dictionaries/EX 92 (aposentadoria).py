dic = dict()

dic['Name'] = str(input("Input your name: "))
birth_year = int(input("Wrote your birth year: "))
age = 2025 - birth_year
dic['Age'] = age
dic['CTPS'] = int(input('Write here your CTPS. [If you do not have one click [0]]: '))

if dic['CTPS'] == 0:
   print()
   for k, v in dic.items():        
        print(f'{k} = {v}')
else:
    year_that_you_started = int(input('Ano de contratação: '))
    dic['Salary'] = float(input('Salary: '))
    dic['aposentadoria'] = 2025 - year_that_you_started 
    print()
    for k, v in dic.items():
        print(f'{k} = {v}')
