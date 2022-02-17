a = float(input('informe a sua altura: '))
b = float(input('informe seu peso: '))
imc = b / (a** 2)
if 18.5 >= imc <= 25:
    print('abaixo do peso.')
elif imc < 18.5:
    print('peso ideal')
elif 25 < imc <= 30:
    print('sobrepeso')
elif 30<imc <= 40:
    print('obesidade')
else:
    print('obesidade morbida')
