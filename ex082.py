a = []
impar =[]
par = []

while True:
    a.append(int(input('insira um valor')))
    s = input('deseja continuar? s-sim (outra tecla)-cancelar')
    if s not in "sS":
        break

for i in a:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'lista com todos valores:{a}\nlista com valres pares:{par}\nlista com valores impares: {impar}')