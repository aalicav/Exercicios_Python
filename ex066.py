c = n = 0
while True:
    num = int(input('Digite um número inteiro[Para parar 999]:'))
    c += 1
    if num == 999:
        break
    n += num
    
print(f'{c} númeroS foram digitados e a soma deles é {n}')