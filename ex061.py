a=int(input('primeiro termo: '))
b=int(input('razão: '))
c=a+(10-1)*b
x=0
#for i in range(a,c+b,b):
while x < 10:
    print(a,end='->')
    a+=b
    x+=1
print('acabou')