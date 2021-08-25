print('''Você pode comprar: 
1.à vista dinheiro ou cheque
2.à vista no cartão
3.2x no cartão
4.3x no cartão''')
op = int(input('Selecione a forma de pagamento:'))
custo = float(input('Quanto custa seu produto? (R$)'))
if op == 1:
  print('O preço do seu produto é {} R$'.format(0.9*preço))
elif op == 2:
  print('O preço do seu produto é {}'.format(0.95*preço))
elif op == 3:
  print('O seu produto não recebe desconto')
elif op == 4: 
  print('O preço do seu produto é {}'.format(1.2*preço))
else:
  print('ERRO! digite um valor da tabela')
