val = float(input('Indique aqui o valor do imóvel(R$):'))
sal = float(input('indique aqui o valor do seu salário(R$):'))
ano = int(input('Em quantos anos você pretende pagar?'))
if val // (ano*12) <= sal*0.3:
    print('Parabéns! Seu empréstimo foi aprovado!')
else:
    print('Infelizmente seu empréstimo não pôde ser aprovado')