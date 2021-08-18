sal = float(input('Digite aqui o seu salário e pressione enter(R$):'))
if sal>1250:
    print('Seu salário com aumento é : {} R$'.format(1.01*sal))
else:
    print('Seu salário com aumento é : {} R$'.format(1.05*sal))