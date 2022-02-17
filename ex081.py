a = []
while True:
    a.append(int(input('insira um valor')))
    s = input('deseja continuar? s-sim (outra tecla)-cancelar')
    if s not in "sS":
        break

print('-'*30)
print(f'ao todo existem {len(a)} numeros na lista')
print(sorted(a, reverse= True))
if 5 in a:
    print('o valor 5 foi encontado na lista.')
else:
    print('o valor 5 não foi encontrado')