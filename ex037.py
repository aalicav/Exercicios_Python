print('''
(1)Converter para Binário
(2)Converter para Hexadecimal
(3)Converter para Octal''')
op = int(input('Escolha uma opção:'))
num = int(input('Escolha um numero inteiro qualquer:'))
if op == 1 :
    print('{} este é o valor {} em binário'.format(op, bin(num)[2:])) 
elif op == 2:
    print('{} este é o valor {} em hexadecimal'.format(op, hex(num)[2:]))
elif op == 3:
    print('{} este é o valor {} em Octal'.format(op, oct(num)[2:]))
else:
    print('Digite um valor aceitável')
