import random
import time
a = int(input('''JOGO DE JOKENPO!!!
1- PEDRA 2- PAPEL 3- TESOURA
'''))
b = random.randint(1,3)
3

print('hummmm')
time.sleep(1)
print('hummmmmm')
time.sleep(1)
print('enquanto você aguarda só quero que saiba que o RYAN é o amor da minha vida.')
time.sleep(2)
if a == 1:
    if b==1:
        print('empate,DROGA.EU JOGUEI PEDRA TAMBEM')
    elif b==2:
        print('HAHA JOGUEI PAPEL SEU PERDEDOR.')
    elif b==3:
        print('HAAAAA DROGA JOGUEI TESOURA...VAMOS DE NOVO,DESSA VEZ VOU GANHAR.')
elif a ==2:
    if b == 1:
        print('HAAAAA DROGA JOGUEI PEDRA...VAMOS DE NOVO,DESSA VEZ VOU GANHAR.')
    elif b == 2:
        print('empate,DROGA.EU JOGUEI PAPEL TAMBEM')
    elif b == 3:
        print('HAHA JOGUEI TESOURA SEU PERDEDOR.')
elif a == 3:
    if b == 1:
        print('HAHA JOGUEI PEDRA SEU PERDEDOR.')
    elif b == 2:
        print('HAAAAA DROGA JOGUEI PAPEL...VAMOS DE NOVO,DESSA VEZ VOU GANHAR.')
    elif b == 3:
        print('empate,DROGA.EU JOGUEI TESOURA TAMBEM')