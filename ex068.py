from random import choice
resultado = choice(['PAR','IMPAR'])
c = 0
while True:
    escolha = str(input('Escolha [Par ou impar]:')).upper().strip()
    if 'PARIMPAR' not in escolha:
        escolha = str(input('Escolha [Par ou impar]:')).upper().strip()
    if escolha != resultado:
        print(f'Você perdeu, mas ganhou {c} vezes consecutivas!')
        break
    else: 
        c += 1
        print('Parabéns!Você ganhou')