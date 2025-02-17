temp = []
main_list = list()
maior = menor = 0

while True:
  temp.append(str(input("Nome: ")))
  temp.append(float(input('Peso: ')))
  
  if len(main_list) == 0: 
    maior = menor = temp[1]
  else:
    if temp[1] > maior:
      maior = temp[1]
    if temp[1] < menor:
      menor = temp[1]
  main_list.append(temp[:])
  temp.clear()

  op = str(input('Deseja continuar? [S/N]: '))
  if op not in 'Ss':
    break

print()
print(f'O total de pessoas cadastradas foi de {len(main_list)}')
print(f'O maior peso foi de {maior}Kg. Peso de',end= '')

for peso in main_list:
  if peso[1] == maior:
    print(f'[{peso[0]}]',end= '')

print(f'O menor peso foi de {menor}Kg. Peso de',end= '')
for peso in main_list:
  if peso[1] == menor:
    print(f'[{peso[0]}]',end= '')
