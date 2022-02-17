a = float(input('insira o valor da casa:'))
b = float(input('insira o salario do comprador:'))
c = float(input('em quantos anos vai pagar:'))
cm = c*12
pcl = a//cm


if pcl <= b * 30/100:
    print('o valor da prestação mensal é de R${} por {} anos.'.format(pcl,c))
else:
    print('emprestimo negado!!')