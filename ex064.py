c = count = soma = 0
while c != 999:
    c = int(input('Digite aqui um número inteiro:'))
    count += 0
    soma += c
    if c == 999:
        print('{} números foram digitados'.format(count))
        print('A soma entre eles é {}'.format(soma-999))
    
