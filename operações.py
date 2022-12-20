while True:
  n1 = int(input('Digite um número: '))
  n2 = int(input('Digite outro número: '))
  print('''[1] soma
[2] subtração
[3] multiplicação
[4] divisão''')
  o = int(input('Informe o número da operação: '))
  if o == 1:
    print('{} + {} = {}'.format(n1, n2, n1+n2))
  elif o == 2:
    print('{} - {} = {}'.format(n1, n2, n1-n2))
  elif o == 3:
    print('{} x {} = {}'.format(n1, n2, n1*n2))
  elif o == 4:
    print('{} : {} = {:.1f}'.format(n1, n2, n1/n2))
  c = str(input('Quer continuar? ')).upper()[0]
  if c == 'N':
    break
