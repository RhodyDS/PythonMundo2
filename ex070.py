nome=[]
prec = []
tot = 0
maisd = 0
mdm = ''
while True:
    nome.append(input('informe o nome do produto: '))
    prec.append(float(input('informe o preço: ')))
    s = input('desejar cadastrar mais?'
              '[s]sim'
              '[n]não')
    if s not in 'SNsn':
        print('informe uma opção valida')
    elif s in 'Nn':
        break

print(f'total gasto: R${tot}')
for i in range(0,len(nome)):
    if prec[i] >1000:
        maisd +=1
    if prec[i] == min(prec):
        mdm= nome[i]
print(f'{maisd} produtos com mais de R$1000')
print(f'produto com menor preço: {mdm}')