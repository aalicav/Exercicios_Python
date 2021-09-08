num = int(input('Digite aqui quanto você quer sacar:'))
num_2 = num
cont = 0
nota = 50
while True:
    if num_2 >= nota:
        num_2 = num_2 - nota
        cont += 1
    else:
        print(f'Você receberá {cont} notas de {nota} R$')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if num_2 == 0:
            break

