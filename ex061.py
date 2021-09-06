a_1 = int(input('Insira aqui o primeiro termo da P.A'))
r = int(input('Insira aqui a razão da P.A'))
c = n = 0 
m = 10
while m != 0:
    n += m
    while c <= n:
        c += 1
        print(a_1+(c-1)*r, end=',')
    m = int(input('\nQuantos números a mais dessa PA você gostaria de ver?'))      

            




    
    
        
    
    
        

