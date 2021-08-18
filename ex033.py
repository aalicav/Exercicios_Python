num1 = float(input('Digite aqui o primeiro numero e pressione enter: '))
num2 = float(input('Digite aqui o segundo numero e pressione enter: '))
num3 = float(input('Digite aqui o terceiro numero e pressione enter: '))
if num1>num2>num3:
    print('{} é o maior numero entre eles e {} é o menor'.format(num1, num3))
if num3>num2>num1:
    print('{} é o maior numero entre eles e {} é o menor'.format(num3, num1))
if num1>num3>num2:
    print('{} é o maior entre eles e {} é o menor'.format(num2,num1))
if num3>num1>num2:
    print('{} é o maior entre eles e {} é o menor'.format(num3,num2))
if num2>num3>num1:
    print('{} é o maior entre eles e {} é o menor'.format(num2,num1))
if num2>num1>num3:
    print('{} é o maior entre eles e {} é o menor'.format(num2,num3))
