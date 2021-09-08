c = cont = maior = menor = num = res = 0
while res != 'N':
    num = int(input('Digite um número inteiro:'))
    res = str(input('Você quer continuar[S/N]?')).upper()
    cont += 1
    if res not in 'SN':
        res = str(input('Digite só S ou N:')).upper()
    c += num
    if cont == 1:
        maior += num
    else:
        if num  > maior:
            maior = num 
        else:
            menor = num
print('A média desses número é {}'.format(c/cont))
print('{} é o maior número e {} é o menor'.format(maior,menor))


