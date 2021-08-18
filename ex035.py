a = float(input('Digite o comprimento do lado "a" do triangulo:'))
b = float(input('Digite o comprimento do lado "b" do triangulo:'))
c = float(input('Digite o comprimento do lado "c" do triangulo:'))
if a+b>c:
    print('{},{},{} são realmente lados de um mesmo triangulo'.format(a,b,c))
else:
    print('{}, {} e {} não são lados de um mesmo triangulo'.format(a,b,c))
