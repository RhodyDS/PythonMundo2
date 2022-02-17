dados = []
dic = {}
list = []
sm = 0
mul = []
while True:
    a = input('insira o nome: ')
    dados.append(input('insira o sexo [m] ou [f]').lower())
    if dados[0] in 'f':
        mul.append(a)
    dados.append(int(input('insira a idade:')))
    sm += dados[1]
    dic[a] = dados[:]
    dados.clear()
    list.append(dic)
    cont = input('deseja continuar \n1 - sim\noutro valor - não?').lower()
    if cont not in '1':
        break

print(f'foram cadastradas {len(dic)}')
print(f'a média de idade do grupo é {sm/len(dic)}')
print(f'todas as mulheres:\n{mul}')
print('lista com pessoas acima da media de idade:')

for x,i in dic.items():
    if i[1]>sm/len(dic):
        print(x)


