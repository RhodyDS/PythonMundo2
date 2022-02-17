def contador(inicio,fim,passo):
    for i in range(inicio,fim,passo):
        print(i)



contador(1,11,1)
contador(10,-1,-2)
print('contagem personalizada')
a=int(input('numero de inicio'))
b = int(input('numero final'))
c = int(input('passo:'))
contador(a,b,c)
