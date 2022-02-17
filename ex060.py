a = int(input('insira um valor:'))
x = a - 1
b=0
while x != -1:
    b += a * x
    print('{}x'.format(a))
    print()
    a = x
    x -= 1
print(b)
