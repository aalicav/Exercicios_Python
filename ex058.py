from random import randint
from time import sleep
print('''Vou pensar num número de 0 a 10, tente advinhar 
....''')
sleep(5)
esc = randint(1,10)
user = int(input('Diga em que número eu pensei:'))
cont = 0
while esc != user: 
    user = int(input('Desculpe, tente de novo:'))
    cont += 1
print('Parabéns, você acertou! e precisou de {} tentativas'.format(cont+1))