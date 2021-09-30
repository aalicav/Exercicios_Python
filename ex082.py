lista = []
pares = []
impares = []
while True:
    valores = int(input('Digite um valor:'))
    lista.append(valores)
    if valores % 2 == 0:
        pares.append(valores)
    else: 
        impares.append(valores)
    continuar = str(input('Quer continuar[S/N]?')).upper().strip()
    if continuar == 'N':
        break
print(f'{lista} esta é a lista de números digitados')
print(f'{pares} estes são os números pares')
print(f'{impares} estes são os números impares')
