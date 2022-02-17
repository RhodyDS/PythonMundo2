maior=0
menor=0

for i in range(1,6):
    a=float(input('peso da pessoa {}'.format(i)))
    if i ==1:
        maior=a
        menor=a
    else:
        if a>maior:
            maior = a
        elif a<menor:
            menor = a
print('o maior peso é de :{}kg e o menor peso é de {}kg'.format(maior,menor))