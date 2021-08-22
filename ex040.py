n1 = float(input('Digite a sua primeira nota :'))
n2 = float(input('Digite a sua segunda nota:'))
media = (n1+n2)/2
if media < 5:
    print('A sua média é {:.1f} e você foi reprovado'.format(media))
elif 5.0 <= media <= 6.9:
    print('A sua média é {:.1f} e você está de recuperação'.format(media))
elif media >= 7:
    print('A sua média é {:.1f} e você está aprovado'.format(media))




