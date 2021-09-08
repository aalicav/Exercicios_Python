c = n = 0
while True:
    num = int(input('Digite um número inteiro:'))        
    if num < 0:
        break
    else:
        for n in range(1, num+1):
            for c in range(1,11):
                tab = str(f'Tabuada do {n}')
                if c ==1:
                    print(f'{tab:-^30}')
                print(f'{n}x{c}={n*c}')
                if c == 10:
                    print('-='*30)
