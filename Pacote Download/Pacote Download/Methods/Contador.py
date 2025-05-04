from time import sleep
def contador(i,f,p):
    """
    Contador
    param: i - inicio da contagem
    param f - término da contagem
    param p - passo da contagem
    Função feita para estudo de lógica de programação por Pedro Henrique Rodrigues de Souza
    """

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    # Contagem crescente
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end= '.. ')
            cont += p
        print('FIM')

    # Contagem decrescente
    if i > f:
        cont = i
        while cont >= f:
            print(cont, end= '.. ', flush= True)
            sleep(0.5)
            cont -= p
        print('FIM')


contador(50,20,15)
