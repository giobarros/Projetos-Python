from random import randint
from time import sleep
print('*'*10)
print('JOKENPÔ')
print('*'*10)
itens = ['pedra', 'papel', 'tesoura']
comp = randint(1, 3)
print('''[0] pedra
[1] papel 
[2] tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('Você jogou {} e o computador jogou {}.'.format(itens[jogador], itens[comp]))
if jogador == 1 and comp == 3 or jogador == 3 and comp == 2 or jogador == 2 and comp == 1:
  print('PARABÉNS, VOCÊ GANHOU!!!')
elif jogador == comp:
  print('EMPATE.')
else:
  print('VOCÊ PERDEU!')
