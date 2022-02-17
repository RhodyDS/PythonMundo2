a = float(input('insira a primeira nota:'))
b = float(input('insira a segunda nota:'))
c = (a + b) / 2
if 5.0 <= c <= 6.9:
    print('RECUPERAÇÃO')
elif c < 5:
    print('REPROVADO')
elif c >= 7:
    print('APROVADO')
