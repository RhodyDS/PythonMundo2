a = []

for i in range(0,5):
    a.append(input('digite um valor:'))
a = tuple(a)
print(a)
print(f'o numero nove pareceu {a.count("9" )} vezes')
print(f'o primeiro numero 3 foi digitado na posição {a.index("3")+1}°')
print('os numeros pares são: ')
for i in a:
    if 0 == int(i) % 2:
        print(i,end=' ')