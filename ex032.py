ano = int(input('Digite um ano e pressione enter: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissesto'.format(ano))
else:
    print('{} não é um ano bissesto'.format(ano))