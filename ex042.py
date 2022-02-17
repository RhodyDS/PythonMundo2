a = float(input('informe o valor da primeira medida do triangulo: '))
b = float(input('informe o valor da segunda medida do triangulo: '))
c = float(input('informe o valor da terceira medida do triangulo: '))
if a < b+c and b < c+ a and c < a+b:
    print('é possivel fazer um triangulo com tais medidas')
    if a == b == c:
        print('triangulo é equilátero.')
    elif a == b or a == c or b == c:
        print('isósceles')
    else:
        print('escaleno')

else:
    print('não é possivel fazer um triangulo com essas medidas.')
