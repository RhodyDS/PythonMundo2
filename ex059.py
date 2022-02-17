cont = 0

while cont == 0:
    a = float(input('insira um valor: '))
    b = float(input('insira outro valor: '))
    menu=int(input('''''
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa
    '''))
    if menu == 1:
        print('a soma entre {} e {} é:{} '.format(a,b,a+b))
    elif menu == 2:
        print('a multiplicação entre {} e {} é {}'.format(a,b,a*b))
    elif menu ==3:
        if a>b:
            print('o numero maior é {}'.format(a))
        elif b>a:
            print('o numero maior é {}'.format(b))
        else:
            print('os dois são numeros iguais.')
    elif menu == 4:
        print('novos valores')
    elif menu == 5:
        print('boa sorte na vida')
        break