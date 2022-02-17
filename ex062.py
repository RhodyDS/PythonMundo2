a=int(input('primeiro termo: '))
b=int(input('razão: '))
c=a+(10-1)*b
cont=1
x=0
#for i in range(a,c+b,b):
while x < 10:
    print(a,end='->')
    a+=b
    x+=1
print('acabou')
while cont!=0:
    cont=int(input('digite algum numero para mostrar o termo da P.A dele?(digite 0 para sair)\n'))
    if cont != 0:
        x=0
        a=cont
        while x < 10:
            print(a, end='->')
            a += b
            x += 1

print('fim do progama')
