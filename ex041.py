idade = int(input('Digite aqui a idade do seu filho:'))
if idade <= 9:
    print('seu filho é da classe MIRIM')
elif 9 < idade <= 14:
    print('Seu filho é da classe INFANTIL')
elif 14 < idade <= 19:
    print('Seu filho é da classe Junior')
elif 19 < idade <= 20:
    print('Seu filho é da classe Sênior')
else:
    print(' Você é MASTER')