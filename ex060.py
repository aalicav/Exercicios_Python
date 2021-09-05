n = int(input('Insira aqui um número:'))
c = 0
i = 1
while n != c:
    c += 1
    if c == n:
        n = c
    else:
        i *= (n-c)
print('5!={}'.format(n*i))






