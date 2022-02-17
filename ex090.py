sit = {}
b = []
a = input('insira o nome:')
z = float(input('insira a media:'))
b.append(z)
if z >6:
    b.append('aprovado.')
else:
    b.append('reprovado')
    sit[a] = b[:]
print(sit)

