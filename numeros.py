numero_extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
while True:
    numero = int(input('Digite um número entre 0 e 10: '))
    if not 0 <= numero <= 10:
        print('Tente novamente...', end=' ')
    else:
        for pos, c in enumerate(numero_extenso):
            if pos == numero:
                print('Você digitou o número {}.'.format(c))
    c = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if c == 'N':
        break
print('FIM!')
