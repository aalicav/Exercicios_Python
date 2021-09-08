prod = gasto = menor = cont = preço = 0
nome_barato = ''
while True:
    nome  = str(input('Digite aqui o nome do produto:')).strip().lower()
    while preço != float(preço):
        preço  = float(input('Digite um valor válido:'))
    preço = float(input('Digite aqui o preço do produto:'))
    continuar = str(input('Quer continuar?[S/N]')).strip().lower()
    if continuar == 'n':
        break
    gasto += preço
    cont  += 1
    if preço > 1000:
        prod += 1
    if cont == 1:
        menor = preço
    else: 
        if preço < menor:
            menor = preço
            nome_barato = nome
print(f'Dos {cont} produtos listados {prod} custam mais de mil reais')
print(f'O gasto total é {gasto}R$')
print(f'{nome} é o produto mais barato')

