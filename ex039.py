ano = int(input('Insira aqui o ano do seu nascimento:'))
import datetime
date = datetime.date.today()
hoje = int(date.strftime("%Y"))
if hoje - ano == 18:
    print('Você já tem {} anos e está na hora de se alistar'.format((hoje - ano)))
elif hoje - ano < 18:
    print('Você só tem {} anos, e você ainda deve se alistar'.format((hoje-ano)))
else:
    print('Você já tem {} anos e passou da idade do alistamento'.format((hoje - ano)))