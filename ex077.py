palavras = ('XICARA','NABO','PADRE','COROINHA','MISSA')
for e in palavras:
    print(f'\n {e} possui as seguintes vogais:',end='')
    for vogal in e:
        if vogal in 'AEIOU':
            print(vogal,end=',')
