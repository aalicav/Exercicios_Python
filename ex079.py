valores = list()
while True:
    num = int(input('Digite um valor:'))
    if valores.count(num)+1 == 2:
        print('Desculpe, valor repetido! Não posso armazena-lo')
    else:
        valores.append(num) 
    continuar = str(input('Quer continuar[S/N]?')).strip().lower()
    if continuar == 'n':
        break
print(sorted(valores))
