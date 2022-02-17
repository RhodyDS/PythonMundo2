frase = input('qual é a frase:')
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]
if inverso==junto:
    print('a frase é palidrono')
else:
    print('a frase não é palidrono.')