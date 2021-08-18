nome = input('Digite o nome da sua cidade e pressione enter:')
nome = nome.lower()
nome = nome.strip()
print('O nome da sua cidade começa com Santo? {}'.format('santo' in nome[0:6]))