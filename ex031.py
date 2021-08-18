d = float(input('Digite quantos quilometros você irá percorrer(km): '))
if d <= 200:
    print('{} R$ é o preço da sua passagem'.format(0.5*d))
else:
    print('{} R$ é o preço da sua passagem'.format(0.45*d))
