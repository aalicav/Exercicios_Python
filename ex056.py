num = 0
maior = 0
cont = 0
nomem = ''
for c in range(1,5):
    nome = input('Digite aqui o nome da {}ª pessoa'.format(c))
    idade = int(input('Digite aqui a idade da {}ª pessoa'.format(c)))
    sexo = str(input('Digite aqui o sexo da {}ª pessoa (Masculino ou Feminino)'.format(c))).upper().strip() 
    num += idade
    med = (num)/4 
    if 'MASCULINO' in sexo :
        if c == 1:
            maior = idade
        else: 
            if idade > maior:
                maior = idade
                nomem = nome
    if 'FEMININO' in sexo:
        if idade < 20:
            cont += 1
print('O homem de maior idade é {} '.format(nomem))
print('O número de mulheres menores de 20 anos é {}'.format(cont))
print('A média da idade destas quatro pessoas é {} anos'.format(med))

    
 