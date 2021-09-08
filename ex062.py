n = int(input('Quantos números da sequencia de Fibonnaci você quer ver?'))
a_0 =1
a_1 =1
c = 0
while c < n+2:
    c +=1
    a_2 = a_1 + a_0
    if c == 1 or c == 2:
        a_0 = 1
        a_1 = 0
    elif c == 0:
        a_0 = 0
        a_1 = 0
    else:
        a_0 = a_1
        a_1 = a_2
        print(a_2,end=',')


