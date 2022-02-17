import random,time

err=0
a = random.randint(0, 10)

b = int(input('tente advinhar o numero que estou pensando de 0 a 10:\n'))
print('processando...')
time.sleep(3)
while err == 0:
    if a == b:
        print('parabens eu pensei no numero {} e você digitou o numero {}!!'.format(a, b))
        err+=1
    else:
        print('você errou!! achei que pudesse ser melhor que isso')
        b=int(input('tente advinhar de novo: '))
        time.sleep(2)