from random import randint
jogador_1 = randint(0, 10)
print('Jogador 1 pensou em um número entre 0 e 10. \nVocê consegue adivinhar?')
acertou = False
jogadas = 0
while not acertou:
    jogador_2 = int(input('Qual é a sua jogada? '))
    jogadas += 1
    if jogador_2 == jogador_1:
        acertou = True
    else:
        if jogador_2 < jogador_1:
            print('Mais...Tente outra vez.')
        elif jogador_2 > jogador_1:
            print('Menos...Tente outra vez.')
print('GANHOU!!! \nVocê jogou {} vez(es)'.format(jogadas))