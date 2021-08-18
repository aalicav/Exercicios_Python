from math import (sin, cos, tan, radians, degrees)
angulo = radians(float(input('Insira um angulo em graus:')))
print('Este é o valor do seno de {:.1f}: {:.2f} \n '
      'Este é o valor do cosseno de {:.1f}: {:.2f} '
      '\n Este é o valor da tangente de {:.1f}: {:.2f}'.format(degrees(angulo), sin(angulo), degrees(angulo), cos(angulo), degrees(angulo), tan(angulo)))