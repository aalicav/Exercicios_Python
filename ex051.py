a1 = float(input('Insira o primeiro termo da progressão:'))
r = float(input('Insira a razão da progressão:'))
for c in range(0,11):
    print('O termo {} dessa P.A é {}'.format(c, a1 + (c-1)*r))
    

