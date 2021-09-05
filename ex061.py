a_1 = int(input('Insira aqui o primeiro termo da P.A'))
r = int(input('Insira aqui a razão da P.A'))
c = 0 
t = False
while t == False:
    c += 1
    if c == 10:
        print(a_1 + (c-1)*r, end=',')
        c = int(input('Você quer mostrar mais fotos? Se sim, diga quantos:'))
        print(a_1 + (c-1)*r, end=',')        
    c = int(input('Você quer mostrar mais fotos? Se sim, diga quantos:'))
    if c == 0:
        t = True

    
    
        
    
    
        

