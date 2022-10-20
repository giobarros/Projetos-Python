lista = [[], []]
numero = 0
for c in range(1,8):
    numero = int(input('Digite o {}° valor: '.format(c)))
    if numero % 2 == 0:
        lista[0].append(numero)
    elif numero % 2 == 1:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print('Os valores pares são {}'.format(lista[0]))
print('Os valores ímpares são {}'.format(lista[1]))