while True:   
    numero = int(input('Informe um valor para ver a tabuada (-1 para parar): '))
    if numero < 0:
        break
    for c in range(0, 11):
        print('{} x {} = {}'.format(numero, c, numero * c))
print('Programa encerrado.')