sexo = str(input('Insira aqui o sexo da pessoa (M ou F):')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Insira aqui o sexo da pessoa (M ou F):')).strip()
    print('Insira somente M ou F')
print('Informação lida com sucesso')

