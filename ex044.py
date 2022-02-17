a = float(input('insira o preço do produto'))
b = float(input('condição de pagamento:\n1-a vista(dinheiro/cheque)\n2-avista no cartao\n3-em até 2x cartão\n4-3x ou mais no cartão'))
if b ==1:
    print('o preço a ser pago é de R${:.2f} reais'.format(a-(a*10/100)))
elif b ==2:
    print('o preço a ser pago é de R${:.2f} reais'.format(a-(a*5/100)))
elif b ==3:
    print('o preço a ser pago é de R${:.2f} reais'.format(a))
elif b==4:
    print('o preço a ser pago é de R${:.2f} reais'.format(a + (a * 20 / 100)))