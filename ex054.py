from datetime import date
data = date.today().year
cont = 0
cont1 = 0
for c in range(1,8):
    ano = int(input('Insira aqui o ano do nascimento da pessoa {}:'.format(c)))
    if data - ano >= 18:
        cont += 1
    else:
        cont1 += 1
print('{} pessoas já são maiores de idade e {} ainda não são'.format(cont, cont1))
