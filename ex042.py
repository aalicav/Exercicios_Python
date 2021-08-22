a = float(input('Digite o comprimento do lado "a" do triangulo:'))
b = float(input('Digite o comprimento do lado "b" do triangulo:'))
c = float(input('Digite o comprimento do lado "c" do triangulo:'))
if c < b+a  and b+c> a and a+c > b and a == b == c:
    print('{},{},{} formam um triangulo equilatero'.format(a,b,c))
elif c < b + a and b+c > a and a+c > b and a == b and b != c:
    print('{},{} e {} formam um triangulo isosceles'.format(a,b, c))
elif a < b+c and a+c > b and a+b > c and a != b != c:
    print('{}, {} e {} formam um triangulo escaleno'.format(a, b, c))
else:
    print('{}, {} e {} não são lados de um mesmo triangulo'.format(a,b,c))