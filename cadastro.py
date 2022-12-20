from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
ano = datetime.now().year
cadastro['Idade'] = ano - idade
ctps = int(input('Carteira de trabalho (digite 0 se não tiver): '))
if ctps != 0:
  cadastro['CTPS'] = ctps
  cadastro['Contratação'] = int(input('Ano de contratação: '))
  cadastro['Salário'] = float(input('Salário: R$'))
  aposentadoria = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - ano)
  cadastro['Idade que irá se aposentar'] = aposentadoria
else:
  cadastro['CTPS'] = 'Não possui carteira de trabalho'
print('-=-' * 20)
for k, v in cadastro.items():
  print('- {} tem o valor: {}'.format(k, v))
