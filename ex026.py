nome = input('Digite aqui uma frase e pressione enter:')
nome = nome.lower()
print('Essa frase possui "a"? {}'.format('a' in nome))
print('Quantas vezes "a" aparece nessa frase? {} vezes'.format(nome.count('a')))
nome = nome.split()
print('A primeira letra "a" aparece na posição: {}'.format(nome.find('a')))
print('A ultima letra "a" aparece na posição {}'.format(nome.rfind('a')))