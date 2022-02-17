from random import randint
b = 0
a = ()
a = list(a)
for i in range(5):
    b = randint(0,10)
    a.append(b)

a = tuple(a)
print(f'o maior valor é {max(a)} e o menor valor é {min(a)}')
print(a)