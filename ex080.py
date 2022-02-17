a = []
maior = 0
menor = 0
for i in range(0,5):
    b = int(input(print('insira um valor:')))
    if b in a:
        print('valor já inserido anteriormente,por favor insira um novo valor')
    else:
        if b > max(a):
            a.append(b)

        elif b < min(a):
            a.insert(a.index(b),b)



print(a)