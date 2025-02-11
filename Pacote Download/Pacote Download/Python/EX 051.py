#P.a

termo1 = int(input("Entre com o primeiro termo:\n")) # a1
razao = int(input("Agora entre com a razão:\n")) # Razao
an = termo1 + (10 - 1) * razao # Formula para o enesimo termo 

for c in range(termo1, an + razao, razao):
    termo1 = (c-1)*razao
    print(f'{c}', end='-> ')  
print('FIM')      