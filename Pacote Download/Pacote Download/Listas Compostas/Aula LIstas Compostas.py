test = list()
test_two = list()
for i in range(0,3):
    test.append(str(input('Insira o seu nome: ')))
    test.append(int(input('Insira a sua idade: ')))
    test_two.append(test[:])
    test.clear() # Limpa a list porque a cada iteração a lista muda de tamanho, senao não ficaria formatado da maneira correta

print(test_two)