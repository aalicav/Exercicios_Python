frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
frasej = ''.join(palavras)
vazio = ''
for letra in range(len(frasej)-1,-1,-1):
    #print(frasej[letra], end='')
    vazio += frasej[letra]
if vazio == frasej:
    print('É um palindromo')
else:
    print('Não é um palindromo')