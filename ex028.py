from random import randint
nump = int(input('Tente advinhar o numero de 0 a 5 que será sorteado:'))
num = randint(0,5)
if num == nump:
    print('Você acertou!')
else:
    print('Você errou :(')