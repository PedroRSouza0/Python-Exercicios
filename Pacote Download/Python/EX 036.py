'''036: Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Insira o valor da casa:\n'))
sal = float(input('Insira o valor do seu salário:\n'))
anos = int(input('Em quantos anos pretende pagar:\n'))
prest = casa / (anos * 12)
minimo = (sal * 30)/100

print('Para pagar uma casa de R${:.2f} em {} anos a pretação será de R${:.2f}.'.format(casa, anos, prest))
if (prest > minimo):
    print('Emprétimo Negado. O seu ')
else:
    print('Emprestimo aceito!!!')
