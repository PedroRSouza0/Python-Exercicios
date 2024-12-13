soma = 0

for c in range(1, 500+1, 2):
    if c % 3 == 0:
        soma = soma + c
print(soma)