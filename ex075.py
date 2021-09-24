tupla = ()
for c in range(1,5):
    valor = int(input(f'Digite o valor {c}:'))
    tupla += (valor, )
print(f'O número 9 aparece na tupla {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O primeiro número 3 aparece na posição {tupla.index(3)}')
print('Os números pares são',end=' ')
for c in range(0,4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
