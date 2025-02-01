num = [1,3,7,8, 1, 2]

num.append(7)
num.insert(2,10)

# del num[0]
num.pop(-2)
num.append(2)

# if 2 in num:
   # num.remove(2)
   # print("Foi removido")

# Remover um elemento que se repete
while 2 in num:
    num.remove(2)
    print('Removi um')
    if 2 not in num:
        print("Removi os dois")

num.sort(reverse= True)    
print(num)


teste = list()
teste.append(2)
teste.append(3)
teste.append(9)

for i, n in enumerate(teste):
    print(f"Na posição {i} tem o valor {n}")

# Leitura dinamica
listao = []
for ii in range(0, 4):
    listao.append(int(input(f'Digite o {ii+1} valor: ')))
for ii in range(0, 4):
    print(listao[ii])

