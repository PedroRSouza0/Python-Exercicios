'''043: '''
# IMC == pesokg/pow(altura,2)

from math import pow
peso = float(input('Digite o seu peso em Kg:\n'))
altura = float(input('Digite a sua altura:\n'))

imc = peso / (altura ** 2)



if imc < 18.5:
    print('Abaixo do Peso {:.1f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('Peso Ideal {:.1f}'.format(imc))
elif 25 < imc <= 30:
    print('SobrePeso {:.1f}'.format(imc))    
elif 30 < imc <= 40:
    print('Obesidade {:.1f}'.format(imc))
elif imc > 40:
    print('Obresidade Mórbida {:.1f}'.format(imc))


