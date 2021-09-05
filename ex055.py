cont = 0
x = []
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa em kg:(kg)'.format(c)))
    x.append(peso)
print('A pessoa que pesa menos tem {} (kg)'.format(min(x)))
print('A pessoa que pesa mais tem {} (kg)'.format(max(x)))
