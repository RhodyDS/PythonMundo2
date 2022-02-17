a=int(input('primeiro termo: '))
b=int(input('razão: '))
c=a+(10-1)*b
for i in range(a,c+b,b):
    print(i,end='->')
print('acabou')