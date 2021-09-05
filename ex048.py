acm1 = 0
acm2 = 0
for c in range(0,500): 
    if c % 2 != 0 and c % 3 == 0:
        acm1 += 1
        acm2 += c
print('A soma dos {} numeros é {}'.format(acm1,acm2))
    
          
    