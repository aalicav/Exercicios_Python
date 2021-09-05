num = int(input('Digite um numero inteiro:'))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('{} é um número primo'.format(num))
else:
    print('Não é número primo')

     
    
        




