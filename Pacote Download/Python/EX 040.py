'''040:'''

nota = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))

media = (nota + nota2)/2

if media < 5.0:
    print('Reprovado com a media de {:.2f}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Recuperação com a media de {:.2f}'.format(media))
elif media >= 7:
    print('Aprovado com a media de {:.2f}'.format(media))    


