n_1 = int(input('Insira aqui o primeiro número:'))
n_2 = int(input('Insira aqui o segundo número:'))

print('''
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

''')
op = int(input('Selecione uma das opções acima:'))


while op != 5 :
    if op == 1:
        print('Esta é a soma destes dois números: {}'.format(n_1+n_2))    
    elif op == 2:
        print('Esta é a multiplicação destes dois números:{}'.format(n_1*n_2))
    elif op == 3:
        if n_1 > n_2 :
            print('{} é maior que {}'.format(n_1,n_2))
        else:
            print('{} é maior que {}'.format(n_2,n_1))
    elif op == 4:
        n_1 = int(input('Insira aqui o primeiro número:'))
        n_2 = int(input('Insira aqui o segundo número:'))
    op = int(input('Indique qual a próxima operação com estes dois números:'))
    print('''
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa

    ''')


