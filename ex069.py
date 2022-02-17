sexo=[]
idade = []
demaior = 0
man = 0
mdm = 0
while True:
    idade.append(int(input('informe a idade do individuo')))
    sexo.append(input('[m]masculino'
                      '[f]femino'))
    s = input('desejar cadastrar mais?'
              '[s]sim'
              '[n]não')
    if s not in 'SNsn':
        print('informe uma opção valida')
    elif s in 'Nn':
        break

for i in range(0,len(idade)):
    if idade[i] >18:
        demaior +=1
    if sexo[i] in 'mM':
        man +=1
    if idade[i]<20 and sexo[i] in 'fF':
        mdm+=1

print(f'{demaior} pessoas tem mais de 18 anos')
print(f'foram cadastrados {man} homens')
print(f'foram cadastrados {mdm} mulheres com menos de 20 anos')

