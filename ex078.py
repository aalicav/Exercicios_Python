valores = list()
for p in range(1,6):
    valores.append(int(input('Digite um valor:')))
print(f'O maior valor é {max(valores)} e está na posição {valores.index(max(valores))+1}, o menor é {min(valores)} e está na posição {valores.index(min(valores))+1}')
