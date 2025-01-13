array = (int(input('Digite um número: ')),
         int(input("Digite outro número: ")),
         int(input('Digite o seu terceiro número: ')),
         int(input('Digite o último número: ')))

print(f"O número 9 foi digitado {array.count(9)} vezes.")
print(f"O número 3 foi digitado na posição {array.index(3) + 1}.")

print('Os valores pares foram: ')
for n in array:
    if n % 2 == 0:
        print(f'{n}', end= ', ')
