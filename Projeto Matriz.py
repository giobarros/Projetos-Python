matriz = [[0, 0, 0] , [0, 0, 0], [0, 0, 0]]
soma = soma_valor = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um número para a matriz [{}, {}]: '.format(l,c)))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c], end=' '))
    print()
print('A soma de todos os valores pares digitados é {}'.format(soma))
for l in range(0, 3):
    soma_valor += matriz[l][c]
print('A soma dos valores da terceira coluna é {}'.format(soma_valor))
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print('O maior valor da segunda linha é {}'.format(maior))
