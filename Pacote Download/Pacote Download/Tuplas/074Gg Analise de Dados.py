from random import randint

# Gera 5 números aleatórios e armazena em uma tupla
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Exibe os números sorteados
print(f"Os números sorteados foram: {', '.join(map(str, numero))}")

# Encontra o maior número
#maior = numero[0]
#for n in numero:
 #   if n > maior:
  #      maior = n


# Exibe o maior número
# print("O maior número sorteado foi {}".format(maior))

print(f"O maior valor sorteado foi {max(numero)}")

menor = numero[0]
for n in numero:
    if n < menor:
        menor = n
print(f"O menor {menor}")        
