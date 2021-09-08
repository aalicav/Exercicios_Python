extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
while True:
    num = int(input('Que número de 0 a 20 você quer ver?'))
    if num > 20:
        break
    print(f'{num} por extenso é {extenso[num]}')
    
