a = []
c = 0


while c <6:
    b = int(input('insiraum valoor'))
    if b not in a:
        a.append(b)
        c+=1
    else:
        print('valor já inserido anteriormente,por favor insira um novo valor')
print(sorted(a))