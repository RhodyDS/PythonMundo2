valor = []
r = 's'
while r in 'sS':
    a = int(input('insira um valor:'))
    valor.append(a)
    r = input('deseja continuar?[s-sim][n-não] \n')
    if r in  'nN':
        print('a media de todos os numeros digitados é de: {:.2f}'.format(sum(valor) / len(valor)))
        print('o menor valor digitado foi: {} e o maior valor foi de {}'.format(min(valor), max(valor)))
        r = input('deseja continuar a digitar valores:?[s-sim][n-não] \n')

