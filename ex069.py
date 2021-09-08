h = m = p = i = 0
while True:
    p += 1
    idade = int(input(f'Digite a idade da pess3oa {p}:'))
    sexo = str(input(f'Qual o sexo da pessoa {p} [Masculino ou Feminino]?')).strip().upper()
    while  sexo not in 'MASCULINOFEMININO':
        sexo = str(input(f'Qual o sexo da pessoa {p} [Masculino ou Feminino]?')).strip().upper()
    continuar = str(input('Quer continuar [S/N]?')).upper().strip()
    while continuar not in 'SN':
        continuar = str(input('Digite só S ou N:')).upper().strip()
    if continuar == 'N':
        break
    if idade > 18:
        i += 1
    if sexo == 'MASCULINO':
        h += 1
    if sexo == 'FEMININO' and idade < 20:
        m += 1
print(f'A quantidade de mulheres com mais de 20 anos é {m}')
print(f'A quantidade de homens com mais de 20 ano é {h}')
print(f'A quantidade de pessoas cadastradas é {p}')
