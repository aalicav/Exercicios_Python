print('Vamos dissecar uma variável?')
var = input('Digite qualquer coisa:')
print('{} pertence à classe {}'.format(var, type(var)))
print('{} é um numero? {} '.format(var,var.isnumeric()))
print('{} é uma palavra ou uma letra? {} '.format(var,var.isalpha()))
print('{} é um alfanumerico? {} '.format(var,var.isalnum()))
print('{} é um titulo? {} '.format(var,var.istitle()))
print('{} é um decimal? {} '.format(var,var.isdecimal()))

