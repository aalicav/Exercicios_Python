expressão = str(input('Digite uma expressão matemática:')).strip()
parentesis = []
for c in expressão:
    if c == '(':
        parentesis.append(c)
    elif c == ')':
        if len(parentesis) > 0:
            parentesis.pop()
        else: 
            parentesis.append(c)
if len(parentesis) == 0:
    print('Tudo certo')
else:
    print('Expressão errada')


    