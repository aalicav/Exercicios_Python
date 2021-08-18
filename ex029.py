vel = float(input('Insira aqui a velocidade do carro(km/h):'))
if vel>80:
    print('Você ultrapassou a velocidade permitida de 80(km/h), esta é sua multa: {} R$'.format((vel-80)*7))