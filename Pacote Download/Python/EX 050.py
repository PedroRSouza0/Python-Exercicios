soma = 0
for c in range(1, 6+1):
    n = int(input('Insira o numero:\n'))
    if n % 2 == 0:
        soma += n
print(soma)        