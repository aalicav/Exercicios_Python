dias = int(input('Digite a quantidade de dias que o carro foi alugado:'))
km = float(input('Digite a quantidade de quilometros percorridos(km): '))
print('O preço a ser pago é {} R$'.format((dias*60+0.15*km)))