a = int(input('insira um valor inteiro:'))

b = int(input('qual será a base de conversão?\n1-binario\n2-octal\n3-hexadecimal'))
if b ==1:
    print(format(a, "b"))
elif b == 2:
    print(format(a, "o"))

elif b == 3:
    print(format(a, "x"))