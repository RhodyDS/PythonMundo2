a = int(input('digite um numero: '))
tot = 0
for c in range(1,a+1):
    if a%c==0:
        tot+=1
if tot == 2:
    print('ele é um numero primo.')
else:
    print('não é primo.')