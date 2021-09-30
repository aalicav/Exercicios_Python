valores = list()
for p in range(0,5):
    num = int(input('Digite um valor inteiro:'))
    if p == 0 or num > valores[-1]:
        valores.append(num)
    else:
        n = 0
        while n < len(valores):
            if num <= valores[n]:
                valores.insert(n,num)
                break
        n += 1            
print(valores)