p = float(input('Digite seu peso em kg:'))
h = float(input('Digite sua altura em metros:'))
imc = p/(h**2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obsidade mórbida')