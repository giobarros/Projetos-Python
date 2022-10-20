tupla = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite outro número: ')))
print('Valores na tupla: {}'.format(tupla))
print('O valor 9 aparece {} vez(es)'.format(tupla.count(9)))
print('O primeiro número 3 aparece na posição {}'.format(tupla.index(3)))