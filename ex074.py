from random import randint
c = 0
número = (randint(1,1000000),)
for c in range(1,6):
    número += (randint(1,100000),)
print(f'Os números sortados são: {número}')
print(f'O maior número sorteado é {max(número)} e o menor é {min(número)}')