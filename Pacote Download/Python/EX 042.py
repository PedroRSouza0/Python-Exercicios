'''042: '''

a = int(input('Digite o valor da primeira reta:\n'))
b = int(input('Digite o valor da segunda reta:\n'))
c = int(input('Digite o valor da ultima reta:\n'))


if a < b + c and b < c + a and a < c + b:
    print("Valores FORMAM um triângulo.")

    if a == b and c == b and c == a:
        print('Triângulo Equilatero')
    if a == b or b == c or c == a:
        print("Triângulo Isóceles")
    elif a != b and c != b and c != a:
        print('Triângulo Escaleno')
else:
    print("Valores não formam um triângulo.")


