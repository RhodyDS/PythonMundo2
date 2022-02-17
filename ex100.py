from random import randint
numeros = []
def sorteio(n):
    for i in range(5):
        n.append(randint(0,10))
    return numeros

def somarPar(n):
    c=0

    for i in n:
        if i %2==0:
            c += i
    print(c)

a = sorteio(numeros)
print(a)
somarPar(a)