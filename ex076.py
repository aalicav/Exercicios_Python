print("LISTA DE PRODUTOS")
tupla = ('Terço', '27,50', 'Caderno', '12,50','Estojo','2,50','Bicicleta','550')
for c in range(0,len(tupla)):
    if c % 2 == 0:
        print(tupla[c],end='-'*20)
    else:
        print(tupla[c])
