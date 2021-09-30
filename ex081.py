lista = []
while True:
    valores = int(input('Digite um valor:'))
    lista.append(valores)
    lista.sort(reverse=True)
    continuar = str(input('Quer continuar[S/N]?')).upper().strip()
    if continuar == 'N':
        break
print(f'{len(lista)} foram digitados')
print(f'Esta é a lista na ordem descrescente: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')