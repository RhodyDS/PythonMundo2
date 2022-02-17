cont = 1


while cont == 1:
    sexo = input('informe F para feminino e M para masculino.').upper()
    if sexo in 'F,M':
        cont += 1
    else:
        print('por favor informe uma opção valida')
